from shapely.geometry import Point, LineString, Polygon


def get_centroid(geometric_object):
    """
    takes any kind of Shapely's geometric -object as
    input and returns a centroid of that geometry.
    :param geometric_object:
    :return: centroid of any geometric object
    """
    return geometric_object.centroid


def get_area(polygon_object):
    """
    takes a Shapely's Polygon -object as input and
    returns the area of that geometry.
    :param polygon_object:
    :return: area of polygon
    """
    return polygon_object.area


def get_length(input_object):
    """
    takes either a Shapely's LineString or Polygon -object 
    as input. Function should check the type of the input 
    and returns the length of the line if input is LineString
     and length of the exterior ring if input is Polygon. 
     If something else is passed to the function, it should 
     tell the user --> 
     "Error: LineString or Polygon geometries required!"
    :param input_object: 
    :return: length of line or polygon
    """
    if isinstance(input_object, LineString) or isinstance(input_object, Polygon):
        return input_object.length
    else:
        return 'Error: LineString or Polygon geometries required!'
