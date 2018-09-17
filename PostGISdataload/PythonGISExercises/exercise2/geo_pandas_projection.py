import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
from shapely.geometry import Point, LineString

if __name__ == '__main__':
    """
    - Download the data (Click on the link ==> CNTRL + S)
    - Read the data into memory using Pandas.
    - Create an empty column called geometry where you will store shapely Point objects.
    - Iterate over the rows of the DataFrame and insert Point objects 
        into column geometry (you need to use .loc indexer to update the row, see materials.
    - Convert that DataFrame into a GeoDataFrame, see hints
    - Update the CRS for coordinate system as WGS84 (i.e. epsg code: 4326)
    - Save the data into a Shapefile called Kruger_posts.shp
    - Create a simple map of those points using a GIS software or using .plot() 
        funtion in Python. Save it to GitHub as png file.
    """
    data_frame = pd.read_csv('/Users/<redacted>/pythonGIS/some_posts.csv')

    data_frame['geometry'] = [Point(xy) for xy in zip(data_frame.lon, data_frame.lat)]

    data_frame_clean = data_frame.drop(['lon', 'lat'], axis=1)

    crs = {'init': 'epsg:4326'}
    geo = gpd.GeoDataFrame(data_frame_clean, crs=crs, geometry=data_frame['geometry'])

    out = r'/Users/<redacted>/pythonGIS/Kruger_posts.shp'

    geo.plot()
    plt.savefig('/Users/<redacted>/pythonGIS/kruger') # file saved in same directory in GitHub

    """
    In this problem the aim is to calculate the distance in meters 
    that the individuals have travelled according the social media 
    posts (Euclidian distances between points).

    Write your codes into the same file as in previous Problem (2).
    
    In your code you should:

    - Re-project the data from WGS84 projection into EPSG:32735 -projection
     which stands for UTM Zone 35S (UTM zone for South Africa) to transform 
     the data into metric system.
    - Group the data by userid
    - Create an empty GeoDataFrame called movements
    - For each user:
        - sort the rows by timestamp
        - create LineString objects based on the points
        - add the geometry and the userid into the GeoDataFrame you created 
        in the last step
    - Determine the CRS of the movements GeoDataFrame to EPSG:32735 (epsg code: 32735)
    - Calculate the lengths of the lines into a new column called distance 
    in movements GeoDataFrame.
    - Save the movements of into a Shapefile called Some_movements.shp
    """
    geo = geo.to_crs(epsg=32735)
    grouped = geo.groupby('userid')
    movements = gpd.GeoDataFrame()
    line_string = LineString(geo)
