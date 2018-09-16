from shapely.geometry import Point, LineString
import pandas as pd


def read_data():
    """
    Read 4 columns, i.e. 'from_x', 'from_y', 'to_x', 'to_y'
    from the data into Python using Pandas.
    :return:
    """
    data_frame = pd.read_csv('travelTimes_2015_Helsinki.txt', sep=';', usecols=['from_x', 'from_y', 'to_x', 'to_y'])
    return data_frame


def iterate(data_frame):
    """Create two lists called orig_points
    and dest_points. Iterate over the rows of your
    DataFrame and add Shapely Point -objects into
    the orig_points-list and dest_point-list
    representing the origin locations and destination
    locations accordingly.
    """
    orig_points, dest_points = [], []
    for index, row in data_frame.iterrows():
        orig_points.append(Point(row['from_x'], row['from_y']))
        dest_points.append(Point(row['to_x'], row['to_y']))
    return orig_points, dest_points

def create_line():
    return None



if __name__ == '__main__':
    print(iterate(read_data()))
