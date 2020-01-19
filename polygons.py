
def decomposition_generator(poly_id: int = 0):
    """Hard coded polygons and decompositions

    Args:
        poly_id (int): Id of the decomposition to generate.

    Returns:
        P (List): Polygon.
        cell_to_site_map (Dict): Map from cell to starting point of robots.
        decomposition (List): Decomposition of polygon P.
    """

    if poly_id == 0:
        P = [[(0.0,0.0),(10.0,0.0),(10.0,1.0),(0.0,1.0)],[]]
        cell_to_site_map = {0: (0,0), 1:(0,0), 2:(0,0), 3:(0,0)}

        decomposition = [[[(0.0,0.0),(10.0,0.0), (10.0,0.5)],[]], [[(0.0,0.0),(10.0,0.5),(10.0,1.0),(5.0,0.5)],[]], [[(5.0,0.5),(10.0,1.0),(0.0,1.0)],[]], [[(0.0,0.0),(5.0,0.5),(0.0,1.0)],[]]]

    elif poly_id == 1:
        P = [[(0.0,0.0),(10.0,0.0),(10.0,1.0),(0.0,1.0)],[]]
        cell_to_site_map = {0: (0,0), 1:(0,1), 2:(10,1), 3:(10,0)}

        decomposition = [[[(0.0,0.0),(2.5,0.0),(2.5,1.0),(0.0,1.0)],[]], [[(2.5,0.0),(5.0,0.0),(5.0,1.0),(2.5,1.0)],[]], [[(5.0,0.0),(7.5,0.0),(7.5,1.0),(5.0,1.0)],[]], [[(7.5,0.0),(10.0,0.0),(10.0,1.0),(7.5,1.0)],[]]]

    elif poly_id == 2:
        P = [[(1.0,0.0),(2.0,0.0),(3.0,1.0),(3.0,2.0),(2.0,3.0),(1.0,3.0),(0.0,2.0),(0.0,1.0)],[]]
        cell_to_site_map = {0: (0,-1), 1:(0,3), 2:(3,-1), 3:(2,3)}
        decomposition = [[[(0.8333333333333334,0.16666666666666666),(0.9285714285714286,1.7857142857142854),(1.0,3.0),(0.0,2.0),(0.0,1.0)],[]], [[(0.9285714285714286,1.7857142857142854),(1.6818181818181817,1.8636363636363633),(3.0,2.0),(2.0,3.0),(1.0,3.0)],[]], [[(1.6818181818181817,1.8636363636363633),(0.9285714285714286,1.7857142857142854),(0.8333333333333334, 0.16666666666666666),(1.0,0.0),(2.0,0.0)], []], [[(1.6818181818181817, 1.8636363636363633), (2.0, 0.0), (3.0, 1.0), (3.0, 2.0)], []]]

    elif poly_id == 3:
        P = [[(0.0, 0.0),(4.0, 0.0),(4.0, 4.0),(6.0, 4.0),(6.0, 0.0),(10.0, 0.0),(10.0, 6.0),(8.0, 7.0),(7.5, 8.0),(10.0, 7.5),(10.0, 10.0),(0.0, 10.0),(0.0, 5.0),(5.0, 6.0),(5.0, 5.0),(0.0, 4.0)],[]]
        cell_to_site_map = {0: (10,0), 1:(10,10), 2:(0,10), 3:(0,0)}

        decomposition = [[[(0.0,0.0),(4.0,0.0),(4.0,4.0),(6.0,4.0),(5.0, 5.0),(0.0, 4.0)],[]],
                         [[(6.0,4.0),(6.0,0.0),(10.0,0.0),(10.0,6.0),(8.0,7.0),(5.0,5.0)],[]],
                         [[(7.5,8.0),(10.0,7.5),(10.0,10.0),(0.0,10.0),(0.0,5.0),(5.0,6.0)],[]],
                         [[(5.0,5.0),(8.0,7.0),(7.5,8.0),(5.0,6.0)],[]]]

    elif poly_id == 4:        
        # A more complex shape with one hole
        P = [[(0.0,0.0),(6.0,0.0),(6.0,5.0),(4.0,5.0),(4.0,3.0),(5.0,3.0),(5.0,2.0),(3.0,2.0),(3.0,6.0),(7.0,6.0),(7.0,0.0),(10.0,0.0),(10.0,10.0),(0.0,10.0)],[[(4.0,7.0),(3.5,8.0),(4.5,9.0),(6.0,8.0)]]]
        cell_to_site_map = {0: (10,0), 1:(10,10), 2:(0,10), 3:(0,0)}

#        decomposition = [[[(6.0,0.0),(6.0,5.0),(4.0,5.0),(4.0,3.0),(5.0,3.0),(5.0,2.0)],[]],
#                         [[(7.0,6.0),(7.0,0.0),(10.0,0.0),(10.0,10.0)],[]],
#                         [[(7.0,6.0),(10.0,10.0),(0.0,10.0),(3.5,8.0),(4.5,9.0),(6.0,8.0)],[]],
#                         [[(0.0,0.0),(6.0,0.0),(5.0,2.0),(3.0,2.0),(3.0,6.0),(7.0,6.0),(6.0,8.0),(4.0,7.0),(3.5,8.0),(0.0,10.0)],[]]]


        decomposition = [[[(6.0,0.0),(6.0,5.0),(4.0,5.0),(4.0,3.0),(5.0,3.0),(5.0,2.0)],[]],
                         [[(7.0,6.0),(7.0,0.0),(10.0,0.0),(10.0,10.0),(6.0,8.0),(4.0,7.0)],[]],
                         [[(6.0,8.0),(10.0,10.0),(0.0,10.0),(3.5,8.0),(4.5,9.0)],[]],
                         [[(0.0,0.0),(6.0,0.0),(5.0,2.0),(3.0,2.0),(3.0,6.0),(7.0,6.0),(4.0,7.0),(3.5,8.0),(0.0,10.0)],[]]]
    elif poly_id == 5:
        # A rectangle
        P = [[(0.0,0.0),(9.0,0.0),(9.0,1.0),(0.0,1.0)],[]]
        cell_to_site_map = {0: (0,0), 1:(0,0), 2:(0,0)}

        #decomposition = [[[(0.0,0.0),(3,0.0),(3,1.0),(0.0,1.0)],[]], [[(3,0.0),(6.0,0.0),(6.0,1.0),(3,1.0)],[]], [[(6.0,0.0),(9.0,0.0),(9.0,1.0),(6.0,1.0)],[]],]
        decomposition = [[[(0.0,0.0),(1.0,0.0),(1.0,1.0),(0.0,1.0)],[]], [[(1.0,0.0),(6.0,0.0),(6.0,1.0),(1.0,1.0)],[]], [[(6.0,0.0),(9.0,0.0),(9.0,1.0),(6.0,1.0)],[]],]

    elif poly_id == 6:
        P = [[(0.0,0.0),(10.0,0.0),(10.0,10.0),(0.0,10.0)],[[(7.0,1.0),(7.0,3.0),(8.0,3.0),(8.0,1.0)],[(1.0,4.0),(1.5,4.5),(3.0,5.0),(3.5,4.5),(3.0,3.0),(2.0,3.0)],[(4.0,7.0),(6.0,9.0),(7.0,8.0),(6.0,7.0),(8.0,6.0),(8.5,6.5),(9.0,6.0),(8.0,5.0)]]]
        cell_to_site_map = {0: (10,0), 1:(10,10), 2:(0,10), 3:(0,0)}        
        
        decomposition = [[[(0.0,0.0),(1.0,4.0),(1.5,4.5),(3.0,5.0),(4.0,7.0),(6.0,9.0),(10.0,10.0),(0.0,10.0)],[]],
                         [[(0.0,0.0),(7.0,1.0),(7.0,3.0),(8.0,5.0),(4.0,7.0),(3.0,5.0),(3.5,4.5),(3.0,3.0),(2.0,3.0),(1.0,4.0)],[]],
                         [[(0.0,0.0),(10.0,0.0),(10.0,10.0),(9.0,6.0),(8.0,5.0),(7.0,3.0),(8.0,3.0),(8.0,1.0),(7.0,1.0)],[]],
                         [[(10.0,10.0),(6.0,9.0),(7.0,8.0),(6.0,7.0),(8.0,6.0),(8.5,6.5),(9.0,6.0)],[]]]

    elif poly_id == 7:
        P = [[(0.0,0.0),(4.0,0.0),(4.0,5.0),(2.0,5.0),(2.0,6.0),(5.0,6.0),(5.0,0.0),(10.0,0.0),(10.0,4.0),(7.0,4.0),(7.0,5.0),(10.0,5.0),(10.0,10.0),(0.0,10.0)],[[(7.0,7.0),(7.0,9.0),(8.0,9.0),(8.0,7.0)],[(3.0,7.0),(2.0,8.0),(3.0,9.0),(6.0,8.0)]]]
        cell_to_site_map = {0: (10,0), 1:(10,10), 2:(0,10), 3:(0,0)}        

        decomposition = [[[(0.0,0.0),(4.0,0.0),(4.0,5.0),(2.0,5.0),(0.0,5.0)],[]],
                         [[(0.0,10.0),(0.0,5.0),(2.0,5.0),(2.0,6.0),(3.0,6.0),(3.0,7.0),(2.0,8.0),(3.0,9.0),(3.0,10.0)],[]],
                         [[(10.0,7.0),(10.0,10.0),(3.0,10.0),(3.0,9.0),(6.0,8.0),(7.0,9.0),(8.0,9.0),(8.0,7.0),],[]],
                         [[(10.0,0.0),(10.0,4.0),(7.0,4.0),(7.0,5.0),(10.0,5.0),(10.0,7.0),(8.0,7.0),(7.0,7.0),(7.0,9.0),(6.0,8.0),(3.0,7.0),(3.0,6.0),(5.0,6.0),(5.0,0.0)],[]]]

    # New combined holes
    elif poly_id == 8:        
        # A more complex shape with one hole
        P = [[(0.0,0.0),(6.0,0.0),(6.0,5.0),(4.0,5.0),(4.0,3.0),(5.0,3.0),(5.0,2.0),(3.0,2.0),(3.0,6.0),(3.9,6.0),(3.9,7.0),(3.5,8.0),(4.5,9.0),(6.0,8.0),(4.1,7.0),(4.1,6.0),(7.0,6.0),(7.0,0.0),(10.0,0.0),(10.0,10.0),(0.0,10.0)],[]]
        cell_to_site_map = {0: (10,0), 1:(10,10), 2:(0,10), 3:(0,0)}

        decomposition = [[[(6.0,0.0),(6.0,5.0),(4.0,5.0),(4.0,3.0),(5.0,3.0),(5.0,2.0)],[]],
                         [[(7.0,6.0),(7.0,0.0),(10.0,0.0),(10.0,10.0),(6.0,8.0),(4.1,7.0),(4.1,6.0)],[]],
                         [[(6.0,8.0),(10.0,10.0),(0.0,10.0),(3.5,8.0),(4.5,9.0)],[]],
                         [[(0.0,0.0),(6.0,0.0),(5.0,2.0),(3.0,2.0),(3.0,6.0),(3.9,6.0),(3.9,7.0),(3.5,8.0),(0.0,10.0)],[]]]

    elif poly_id == 9:
        P = [[(0.0,0.0),(7.0,0.0),(7.0,3.0),(7.4,3.0),(7.9,5.0),(4.1,7.0),(3.1,5.0),(3.5,4.5),(3.0,3.0),(2.0,3.0),(1.0,4.0),(1.5,4.5),(2.9,5.0),(3.9,7.0),(6.0,9.0),(7.0,8.0),(6.0,7.0),(8.0,6.0),(8.5,6.5),(9.0,6.0),(8.1,5.0),(7.6,3.0),(8.0,3.0),(8.0,0.0),(10.0,0.0),(10.0,10.0),(0.0,10.0)],[]]
        cell_to_site_map = {0: (10,0), 1:(10,10), 2:(0,10), 3:(0,0)}    
        
        decomposition = [[[(0.0,0.0),(1.0,4.0),(1.5,4.5),(2.9,5.0),(3.9,7.0),(6.0,9.0),(10.0,10.0),(0.0,10.0)],[]],
                         [[(0.0,0.0),(7.0,0.0),(7.0,3.0),(7.4,3.0),(7.9,5.0),(4.1,7.0),(3.1,5.0),(3.5,4.5),(3.0,3.0),(2.0,3.0),(1.0,4.0)],[]],
                         [[(8.0,0.0),(10.0,0.0),(10.0,6.0),(9.0,6.0),(8.1,5.0),(7.6,3.0),(8.0,3.0)],[]],
                         [[(10.0,10.0),(6.0,9.0),(7.0,8.0),(6.0,7.0),(8.0,6.0),(8.5,6.5),(9.0,6.0),(10.0,6.0)],[]]]

    elif poly_id == 10:
        P = [[(0.0,0.0),(4.0,0.0),(4.0,5.0),(2.0,5.0),(2.0,6.0),(5.0,6.0),(5.0,0.0),(10.0,0.0),(10.0,4.0),(7.0,4.0),(7.0,9.0),(8.0,9.0),(8.0,5.0),(10.0,5.0),(10.0,10.0),(3.1,10.0),(3.1,9.0),(6.0,8.0),(3.0,7.0),(2.0,8.0),(2.9,9.0),(2.9,10.0),(0.0,10.0)],[]]
        cell_to_site_map = {0: (10,0), 1:(10,10), 2:(0,10), 3:(0,0)}    

        decomposition = [[[(0.0,0.0),(4.0,0.0),(4.0,5.0),(2.0,5.0),(0.0,5.0)],[]],
                         [[(0.0,10.0),(0.0,5.0),(2.0,5.0),(2.0,6.0),(3.0,6.0),(3.0,7.0),(2.0,8.0),(2.9,9.0),(2.9,10.0)],[]],
                         [[(10.0,5.0),(10.0,10.0),(3.1,10.0),(3.1,9.0),(6.0,8.0),(7.0,9.0),(8.0,9.0),(8.0,5.0)],[]],
                         [[(10.0,0.0),(10.0,4.0),(7.0,4.0),(7.0,9.0),(6.0,8.0),(3.0,7.0),(3.0,6.0),(5.0,6.0),(5.0,0.0)],[]]]




    return P, cell_to_site_map, decomposition
