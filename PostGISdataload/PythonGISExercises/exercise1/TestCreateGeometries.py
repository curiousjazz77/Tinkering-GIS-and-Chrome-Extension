from create_geometries import createPointGeom, createLineGeom, createPolyGeom
from shapely.geometry import Point, Polygon, LineString
import unittest

point_1 = Point(5, 6)
point_list = [Point(1.0, 3.5), Point(5.5, 14.1), Point(10.11, -25.312)]
line1 = LineString(point_list)


class TestCreateGeometries(unittest.TestCase):
    """
    Positive tests first. Then negative
    """
    def test_create_point_geom(self):
        generated_pt = createPointGeom(5, 6)
        self.assertEqual(generated_pt, point_1)

    def test_create_line_geom(self):
        point_list2 = [Point(1.0, 3.5), Point(5.5, 14.1), Point(10.11, -25.312)]
        generated_list = createLineGeom(point_list2)
        self.assertEqual(generated_list, point_list2)


