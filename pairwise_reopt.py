import logging

from shapely.geometry import Polygon
from shapely.geometry import LineString

from numpy import linspace
from itertools import product

from chi import compute_chi
from polygon_split import polygon_split


RADIUS = 0.1
LINEAR_PENALTY = 1		# Weights for the cost function
ANGULAR_PENALTY = 10	# Weights for the cost function


# Configure logging properties for this module
logger = logging.getLogger("pairwiseReoptimization")
fileHandler = logging.FileHandler("logs/pairwiseReoptimization.log")
streamHandler = logging.StreamHandler()
logger.addHandler(fileHandler)
logger.addHandler(streamHandler)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

fileHandler.setFormatter(formatter)
streamHandler.setFormatter(formatter)
logger.setLevel(logging.INFO)


def poly_shapely_to_canonical(polygon=[]):
	"""
	A simple helper function to convert a shapely object representing a polygon
	intop a cononical form polygon.

	Args:
		polygon: A shapely object representing a polygon

	Returns:
		A polygon in canonical form.
	"""

	if not polygon:
		return []

	canonicalPolygon = []
	
	if polygon.exterior.is_ccw:
		polyExterior = list(polygon.exterior.coords)
	else:
		polyExterior = list(polygon.exterior.coords)[::-1]


	holes = []
	for hole in polygon.interiors:
		if hole.is_ccw:
			holes.append(list(polygon.exterior.coords)[::-1])
		else:
			holes.append(list(polygon.exterior.coords))

	canonicalPolygon.append(polyExterior)
	canonicalPolygon.append(holes)

	return canonicalPolygon


def compute_pairwise_optimal(polygonA=[],
							 polygonB=[],
							 robotAInitPos=[],
							 robotBInitPos=[],
							 nrOfSamples=100,
							 radius = 0.1,
							 linPenalty = 1.0,
							 angPenalty = 10*1.0/360):
	"""
	Takes two adjacent polygons and attempts to modify the shared edge such that
	the metric chi is reduced.

	TODO:
		Need to investigate assignment of cells to robots.

	Args:
		polygonA: First polygon in canonical form.
		polygonB: Second polygoni n canonical form.
		robotAInitPos: Location of robot A.
		robotBInitPos: Location of robot B.
		nrOfSamples: Samppling density to be used in the search for optimal cut.

	Returns:
		Returns the cut that minimizes the maximum chi metrix. Or [] if no such
		cut exists or original cut is the best.
	
	"""

	# The actual algorithm:
	# 1) Combine the two polygons
	# 2) Find one cut that works better
	# 3) Return that cut or no cut if nothing better was found

	if not polygonA or not polygonB:
		logger.warn("Pairwise reoptimization is requested on an empty polygon.")
		return []

	if not robotAInitPos or not robotBInitPos:
		logger.warn("Pairwise reoptimization is requested on an empty init pos.")
		return []

	if not Polygon(*polygonA).is_valid or not Polygon(*polygonB).is_valid:
		logger.warn("Pariwise reoptimization is requested on invalid polygons.")
		return []

	if not Polygon(*polygonA).is_valid or not Polygon(*polygonB).is_valid:
		logger.warn("Pariwise reoptimization is requested on invalid polygons.")
		return []

	if not Polygon(*polygonA).is_simple or not Polygon(*polygonB).is_simple:
		logger.warn("Pariwise reoptimization is requested on nonsimple polygons.")
		return []

	if not Polygon(*polygonA).touches(Polygon(*polygonB)):
		logger.warn("Pariwise reoptimization is requested on nontouching polys.")
		return []


	# Check that the polygons intersect only at the boundary and one edge
	intersection = Polygon(*polygonA).intersection(Polygon(*polygonB))


	if type(intersection) is not LineString:
		logger.warn("Pariwise reoptimization is requested but they don't touch\
				   at an edge.")
		return []


	# Combine the two polygons
	polygonUnion = Polygon(*polygonA).union(Polygon(*polygonB))
    
    # Also create a copy of polygonUnion in canonical form
	polygonUnionCanon = poly_shapely_to_canonical(polygonUnion)

	if not polygonUnion.is_valid or not polygonUnion.is_simple:
		logger.warn("Pariwise reoptimization is requested but the union resulted\
				   in bad polygon.")
		return []

	if type(polygonUnion) is not Polygon:
		logger.warn("Pariwise reoptimization is requested but union resulted in\
				   non polygon.")
		return []



	# Perform intialization stage for the optimization
	# Initializae the search space as well original cost
	polyExterior = polygonUnion.exterior
	searchDistances = list(linspace(0, polyExterior.length, nrOfSamples))

	searchSpace = []
	for distance in searchDistances:
		solutionCandidate = polyExterior.interpolate(distance)
		searchSpace.append((solutionCandidate.x, solutionCandidate.y))


	# Record the costs at this point
	chiL = compute_chi(polygon = polygonA,
						initPos = robotAInitPos,
						radius = radius,
						linPenalty = linPenalty,
						angPenalty = angPenalty)
	chiR = compute_chi(polygon = polygonB,
						initPos = robotBInitPos,
						radius = radius,
						linPenalty = linPenalty,
						angPenalty = angPenalty)

	initMaxChi = max(chiL, chiR)

	minMaxChiFinal = 10e10
	minCandidate = []

	# This search is over any two pairs of samples points on the exterior
	# It is a very costly search.
	for cutEdge in product(searchSpace, repeat=2):

		logger.debug("polygonUnionCanon: %s"%polygonUnionCanon)
		logger.debug("Cut candidate: %s"%(cutEdge, ))
		
		result = polygon_split(polygonUnion, LineString(cutEdge))

		if result:
			logger.debug("%s Split Line: %s"%('GOOD', cutEdge,))
		else:
			logger.debug("%s Split Line: %s"%("BAD ", cutEdge))

		if result:
			# Resolve cell-robot assignments here.
			# This is to avoid the issue of cell assignments that
			# don't make any sense after polygon cut.
			chiA0 = compute_chi(polygon = poly_shapely_to_canonical(result[0]),
							   	initPos = robotAInitPos,
							   	radius = radius,
							   	linPenalty = linPenalty,
							   	angPenalty = angPenalty)
			chiA1 = compute_chi(polygon = poly_shapely_to_canonical(result[1]),
							   	initPos = robotAInitPos,
							   	radius = radius,
							   	linPenalty = linPenalty,
							   	angPenalty = angPenalty)
			chiB0 = compute_chi(polygon = poly_shapely_to_canonical(result[0]),
							   	initPos = robotBInitPos,
							   	radius = radius,
							   	linPenalty = linPenalty,
							   	angPenalty = angPenalty)							   	
			chiB1 = compute_chi(polygon = poly_shapely_to_canonical(result[1]),
							   	initPos = robotBInitPos,
							   	radius = radius,
							   	linPenalty = linPenalty,
							   	angPenalty = angPenalty)

			maxChiCases = [max(chiA0, chiB1),
					  	   max(chiA1, chiB0)]

			minMaxChi = min(maxChiCases)
			if minMaxChi <= minMaxChiFinal:
				minCandidate = cutEdge
				minMaxChiFinal = minMaxChi

	logger.debug("Computed min max chi as: %4.2f"%minMaxChiFinal)
	logger.debug("Cut: %s"%(minCandidate, ))

	if initMaxChi < minMaxChiFinal:
		logger.debug("No cut results in minimum altitude")
	
		return []

	newPolygons = polygon_split(polygonUnion, LineString(minCandidate))
	return newPolygons


if __name__ == '__main__':

	P1 = [[(0, 0), (1, 0), (1, 1), (0, 1)], []]
	P2 = [[(1, 0), (2, 0), (2, 1), (1, 1)], []]
	initA = (0, 0)
	initB = (1, 0)
	result = "PASS" if not compute_pairwise_optimal(P1, P2, initA, initB) else "FAIL"
	print("[%s] Simple two polygon test."%result)

	P1 = [[(0, 0), (1, 0), (1, 1), (0, 1)], []]
	P2 = [[(1, 0), (2, 0), (2, 1), (1, 1)], []]
	initA = (0, 0)
	initB = (0, 0)
	print compute_pairwise_optimal(P1, P2, initA, initB)

	P1 = [[(0, 0), (1, 0), (1, 1), (0, 1)], []]
	P2 = [[(1, 0), (2, 0), (2, 1), (1, 1)], []]
	initA = (0, 0)
	initB = (0, 1)
	print compute_pairwise_optimal(P1, P2, initA, initB)	
