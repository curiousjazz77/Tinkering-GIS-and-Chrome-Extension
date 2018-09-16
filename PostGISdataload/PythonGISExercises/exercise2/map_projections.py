import descartes
from fiona.crs import from_epsg
import geopandas as gpd
import matplotlib.pyplot as plt
import pycrs

if __name__ == '__main__':
    # Filepath to the Europe borders Shapefile
    fp = "/Users/<redacted>/pythonGIS/Europe_borders/Europe_borders.shp"

    # Read data
    data = gpd.read_file(fp)
    print(data.crs)
    print(data['geometry'].head())

    # Let's take a copy of our layer
    data_proj = data.copy()

    # Reproject the geometries by replacing the values with projected ones
    data_proj = data_proj.to_crs(epsg=3035)
    data_proj['geometry'].head()

    """To really understand what is going on, it is good to explore 
    our data visually. Hence, let’s compare the datasets by 
    making maps out of them.
    """

    # Plot the WGS84
    data.plot(facecolor='gray')

    # Add title
    plt.title("WGS84 projection")

    # Remove empty white space around the plot
    plt.tight_layout()

    # Plot the one with ETRS-LAEA projection
    data_proj.plot(facecolor='blue')

    #save
    plt.savefig('/Users/<redacted>/pythonGIS/Europe_borders/WGS84projection')

    # Add title
    plt.title("ETRS Lambert Azimuthal Equal Area projection")

    # Remove empty white space around the plot
    plt.tight_layout()

    #save
    plt.savefig('/Users/<redacted>/pythonGIS/Europe_borders/WGS84projection_2')

    # Determine the CRS of the GeoDataFrame
    data_proj.crs = from_epsg(3035)

    # Let's see what we have
    print("data proj crs: ", data_proj.crs)

    """
    Finally, let’s save our projected layer into a Shapefile 
    so that we can use it later.
    """

    # Ouput file path
    outfp = r"/Users/<redacted>/pythonGIS/Europe_borders/Europe_borders_epsg3035.shp"

    # Save to disk
    data_proj.to_file(outfp)


    """
    PyCRS package is a handy library for dealing with projections. 
    If you have the package installed (see installation directions), 
    you can easily convert crs information between EPSG and ESRI codes 
    and Proj4 specification. We can pass the Proj4 text into GeoDataFrame 
    as follows:"""

    crs_info = pycrs.parser.from_epsg_code(3035)

    # Now we have a CRS object
    print(crs_info)

    # Convert to Proj4 specification string
    proj4_txt = crs_info.to_proj4()

    print(proj4_txt)

    # Now we have a correct Proj4 text that we can pass to GeoDataFrame
    data_proj.crs = proj4_txt

    # Same thing as a one-liner
    data_proj.crs = pycrs.parser.from_epsg_code(3035).to_proj4()
