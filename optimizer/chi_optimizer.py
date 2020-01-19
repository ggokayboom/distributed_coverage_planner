"""High level optimizer that runs iterations."""
from shapely.geometry import LineString, Polygon, Point

from decomposition_processing import compute_adjacency
from chi import compute_chi
from reopt_recursion import dft_recursion
from log_utils import get_logger


logger = get_logger("reoptimizer")


class ChiOptimizer():
    __slots__ = (
        'num_iterations',
        'radius',
        'lin_penalty',
        'ang_penalty',
    )

    def __init__(self,
                 num_iterations: int = 10,
                 radius: float = 0.1,
                 lin_penalty: float = 1.0,
                 ang_penalty: float = 10 * 1.0 / 360.):
        self.num_iterations = num_iterations
        self.radius = radius
        self.lin_penalty = lin_penalty
        self.ang_penalty = ang_penalty

    def run_iterations(self,
                       decomposition,
                       cell_to_site_map,
                       original_chi_costs,
                       new_chi_costs):
        """
        Performs pairwise reoptimization on the poylgon with given robot initial
        position.
    
        Args:
            cell_to_site_map
            decomposition: A set of polygon representing the decomposition
            original_chi_costs:  List for storing original costs
            new_chi_cost: List for storing costs after reoptimization.
            num_iterations: The number of iterations or reoptimization cuts to make
            radius: The radius of the coverage footprint
            lin_penalty: A parameter used in the cost computation
            ang_penalty: A parameter used in the cost computation
        Returns:
            N/A
        """
        # TODO: Temporary w.a. until we can switch to Polygon object upstream.
        # pylint: disable=import-outside-toplevel
        from copy import deepcopy
    
        orig_decom = deepcopy(decomposition)
        orig_cell_map = deepcopy(cell_to_site_map)
    
        decomposition = [Polygon(*poly) for poly in orig_decom]
        cell_to_site_map = {key: Point(val) for key, val in orig_cell_map.items()}
    
    
        # Store perf stats for monitoring performance of the algorithm.
        chi_costs = []
        for idx, _ in enumerate(decomposition):
            cost = compute_chi(polygon=decomposition[idx],
                               init_pos=cell_to_site_map[idx],
                               radius=self.radius,
                               lin_penalty=self.lin_penalty,
                               ang_penalty=self.ang_penalty)
            chi_costs.append((idx, cost))
    
        sorted_chi_costs = sorted(chi_costs, key=lambda v: v[1], reverse=True)
        original_chi_costs.extend(sorted_chi_costs)
    
        for i in range(self.num_iterations):
            chi_costs = []
            for idx, _ in enumerate(decomposition):
                cost = compute_chi(polygon=decomposition[idx],
                                   init_pos=cell_to_site_map[idx],
                                   radius=self.radius,
                                   lin_penalty=self.lin_penalty,
                                   ang_penalty=self.ang_penalty)
                chi_costs.append((idx, cost))
            sorted_chi_costs = sorted(chi_costs, key=lambda v: v[1], reverse=True)
    
            logger.debug("Iteration: %3d/%3d: Costs: %s", i, self.num_iterations, sorted_chi_costs)
    
            adjacency_matrix = compute_adjacency(decomposition)
    
            if not dft_recursion(decomposition,
                                 adjacency_matrix,
                                 sorted_chi_costs[0][0],
                                 cell_to_site_map,
                                 self.radius,
                                 self.lin_penalty,
                                 self.ang_penalty):
                logger.debug("Iteration: %3d/%3d: No cut was made!", i, self.num_iterations)
    
            logger.debug("[%3d]: %s\n", i+1, sorted_chi_costs)
    
        # Output new sorted costgs
        chi_costs = []
        for idx, _ in enumerate(decomposition):
            cost = compute_chi(polygon=decomposition[idx],
                               init_pos=cell_to_site_map[idx],
                               radius=self.radius,
                               lin_penalty=self.lin_penalty,
                               ang_penalty=self.ang_penalty)
            chi_costs.append((idx, cost))
        sorted_chi_costs = sorted(chi_costs, key=lambda v: v[1], reverse=True)
        new_chi_costs.extend(sorted_chi_costs)
    
        logger.debug("[%3d]: %s\n", i+1, sorted_chi_costs)
    
        return decomposition


if __name__ == '__main__':

    # If package is launched from cmd line, run sanity checks
    print("\n_sanity tests for the reoptimizer.\n")

    q = {0: (0.0,0.0), 1: (10.0,0.0), 2: (10.0,1.0), 3: (0.0,1.0)}
    decomposition = [[[(0.0,0.0),(10.0,0.0), (10.0,0.5)],[]], [[(0.0,0.0),(10.0,0.5),(10.0,1.0),(5.0,0.5)],[]], [[(5.0,0.5),(10.0,1.0),(0.0,1.0)],[]], [[(0.0,0.0),(5.0,0.5),(0.0,1.0)],[]]]

    optimizer = ChiOptimizer()

    optimizer.run_iterations(decomposition=decomposition,
                             cell_to_site_map=q,
                             original_chi_costs=[],
                             new_chi_costs=[])
