import descartes
import fiona
from fiona.crs import from_epsg
import geopandas as gpd
import matplotlib
import os
import pandas as pd
from shapely.geometry import Point, Polygon


if __name__ == '__main__':
    file_path = "/Users/<redacted>/pythonGIS/Data/DAMSELFISH_distributions.shp"
    data = gpd.read_file(file_path)
    print("data type: ", type(data))
    print(data.head())
    print(data.plot())

    # Create a output path for the data
    out = r"/Users/<redacted>/pythonGIS/Data/DAMSELFISH_distributions_SELECTION.shp"

    # Select first 50 rows
    selection = data[0:50]

    # Write those rows into a new Shapefile (the default output file format is Shapefile)
    selection.to_file(out)

    print("checking out the column in data: ", "\n", data['geometry'].head())
    selection = data[0:5]

    for index, row in selection.iterrows():
        poly_area = row['geometry'].area
        print("Polygon area at index {0} is: {1:.3f}".format(index, poly_area))

    # Let’s next create a new column into our GeoDataFrame where we calculate
    data['area'] = data.area
    print("added data column: ", data['area'].head(2))

    # Maximum area
    max_area = data['area'].max()

    # Mean area
    mean_area = data['area'].mean()

    print("Max area: %s\nMean area: %s" % (round(max_area, 2), round(mean_area, 2)))

    # Create an empty geopandas GeoDataFrame
    newdata = gpd.GeoDataFrame()
    print("empty data set ", newdata)

    # Let’s create a new column called geometry that will contain our Shapely objects:

    # Create a new column called 'geometry' to the GeoDataFrame
    newdata['geometry'] = None

    # Let's see what's inside
    print("new data after column add: ", newdata)

    # Let’s create a Shapely Polygon repsenting the Helsinki Senate square that we can insert to our GeoDataFrame:

    # Coordinates of the Helsinki Senate square in Decimal Degrees
    coordinates = [(24.950899, 60.169158), (24.953492, 60.169158), (24.953510, 60.170104), (24.950958, 60.169990)]

    # Create a Shapely polygon from the coordinate-tuple list
    poly = Polygon(coordinates)

    # Let's see what we have
    print("poly: ", poly)

    # Insert the polygon into 'geometry' -column at index 0
    newdata.loc[0, 'geometry'] = poly

    # Let’s add another column to our GeoDataFrame called Location with text Senaatintori.
    # Add a new column and insert data
    newdata.loc[0, 'Location'] = 'Senaatintori'

    # Let's check the data
    print("new data after column add: ", newdata)

    """GeoDataFrame has a property called .crs that 
    (more about projection on next tutorial) shows the 
    coordinate system of the data which is empty (None) 
    in our case since we are creating the data from the scratch:
    """

    print("crs: ", newdata.crs)

    """Let’s add a crs for our GeoDataFrame. A Python module called fiona 
    has a nice function called from_epsg() for passing coordinate system for 
    the GeoDataFrame. Next we will use that and determine the projection to 
    WGS84 (epsg code: 4326):
    """

    # Set the GeoDataFrame's coordinate system to WGS84
    newdata.crs = from_epsg(4326)  # from fiona import

    # Let's see how the crs definition looks like
    print("crs definition: ", newdata.crs)

    """
    Finally, we can export the data using GeoDataFrames .to_file() -function. 
    The function works similarly as numpy or pandas, but here we only need 
    to provide the output path for the Shapefile. Easy isn’t it!:
    """
    # Determine the output path for the Shapefile
    outfp = r"/Users/<redacted>/pythonGIS/Data/Senaatintori.shp"

    # Write the data into that Shapefile
    newdata.to_file(outfp)

    """
    Practical example: Save multiple Shapefiles
    One really useful function that can be used in Pandas/Geopandas 
    is .groupby(). We saw and used this function already in Lesson 5 
    of the Geo-Python course. Group by function is useful to group data 
    based on values on selected column(s).
    
    Let’s group individual fishes in DAMSELFISH_distribution.shp 
    and export the species to individual Shapefiles.
    Note: If your `data` -variable doesn’t contain the Damselfish 
    data anymore, read the Shapefile again into memory using 
    `gpd.read_file()` -function

    """
    # Group the data by column 'BINOMIAL'
    data = gpd.read_file(file_path)
    grouped = data.groupby('BINOMIAL')

    # Let's see what we got
    print("grouped: ", grouped)

    """
    groupby -function gives us an object called DataFrameGroupBy 
    which is similar to list of keys and values (in a dictionary) 
    that we can iterate over.
    """
    #global individual_fish

    # Iterate over the group object
    for key, values in grouped:
        individual_fish = values
        print("key", key)
        print("values", values)

    # Let's see what is the LAST item that we iterated
        print("individual fish: ", individual_fish)

    """
    From here we can see that an individual_fish variable 
    now contains all the rows that belongs to a fish called 
    Teixeirichthys jordani. Notice that the index numbers 
    refer to the row numbers in the original data -GeoDataFrame.
    """
    print("type of individual fish: ", type(individual_fish))

    """
    As can be seen from the example above, each set of data are now 
    grouped into separate GeoDataFrames that we can export into 
    Shapefiles using the variable key for creating the output filepath 
    names. Here we use a specific string formatting method to produce 
    the output filename using % operator (read more here). Let’s now 
    export those species into individual Shapefiles.
    """
    # Determine outputpath
    outFolder = r"Users/<redacted>/pythonGIS/Data/"

    # Create a new folder called 'Results' (if does not exist) to that folder using os.makedirs() function
    resultFolder = os.path.join(outFolder, 'Results')
    print("result folder: ", resultFolder)
    if not os.path.exists(resultFolder):
        os.makedirs(resultFolder)

    # Iterate over the
    for key, values in grouped:
        # Format the filename (replace spaces with underscores)
        outName = "%s.shp" % key.replace(" ", "_")

        # Print some information for the user
        print("Processing: %s" % key)

        # Create an output path
        outpath = os.path.join(resultFolder, outName)

        # Export the data
        print("out path: ", outpath)
        values.to_file(outpath)



