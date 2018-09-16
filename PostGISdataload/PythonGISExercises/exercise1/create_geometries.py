from shapely.geometry import Point, Polygon, LineString


def createPointGeom(x_coord, y_coord):
    """
    Function should create a shapely Point geometry object and
    return that. Demonstrate the usage of the function by
    creating Point -objects with the function.

    :param x_coord:
    :param y_coord:
    :return: a shapely Point geometry object
    """
    # Create Point geometric object(s) with coordinates
    return Point(x_coord, y_coord)


def createLineGeom(point_list):
    """
    Create a function called createLineGeom() that takes a list of
    Shapely Point objects as parameter and returns a
    LineString object of those input points. Function
    should first check that the input list really contains
    Shapely Point(s). Demonstrate the usage of the function by
    creating LineString -objects with the function.
    :param point_list:
    :return: Line String
    """
    if all(isinstance(pt, Point) for pt in point_list):
        return LineString(point_list)
    else:
        return 'Invalid input. All items in point list are not type Point'
    # example_pt = Point(2.2, 4.2)
    # point_type = type(example_pt)
    # for pt in point_list:
    #     if type(pt) != point_type:
    #         return 'Invalid input'
    #     else:
    #         continue
    # line = LineString(point_list)
    # return line


def createPolyGeom(list_coords_or_pts):
    """
    Create a function called createPolyGeom() that takes
     a list of coordinate tuples OR a list of Shapely
     Point objects and creates/returns a Polygon object
      of the input data. Both ways of passing the data
      to the function should be working. Demonstrate
      the usage of the function by passing data first
      with coordinate-tuples and then with Point -objects.

    Creating a Polygon -object continues the same logic
    of how Point and LineString were created but Polygon
    object only accepts coordinate-tuples as input.
    Polygon needs at least three coordinate-tuples:
    :param list_coords_or_pts:
    :return: Polygon
    """
    for item in list_coords_or_pts:
        return Polygon([[pt.x, pt.y] for pt in list_coords_or_pts])
    else:
        return 'Invalif input. Input must contain point objects or point tuples'
