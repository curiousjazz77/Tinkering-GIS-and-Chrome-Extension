# Using PostgreSQL for data analysis & visualization

General Information

1. Columnar (Redshift, BigQuery) vs Row-based (MySQL, PostgreSQL) DBs:
    - https://www.flydata.com/blog/whats-unique-about-a-columnar-database/
    
2. Data types:
    - `Some examples of geometry subtypes are POINTZ, POINT, LINESTRING, LINESTRINGM, POLYGON, POLYGONZ, POLYHERALSURFACE, POLYHEDRALSURFACEZ, TIN, and TINZ. A typical type declaration in PostGIS is geometry(POINT,4326), where geometry is the data type, POINT is the subtype type modifier, and 4326 is the SRID type modifier.`
    - Point: Subtypes of points differentiate themselves by the dimension of the Cartesian space they occupy.
    - Linestrings: Connected straight lines between two or more distinct points form linestrings. Individual lines between points are called segments. Segments aren’t data types or subtypes in PostGIS, but it is possible for a linestring to have just one segment.
    - Polygons: Closed linestrings are the building blocks of polygons.
    
3. Using Python with GIS
    - https://automating-gis-processes.github.io/CSC18/lessons/L1/Intro-Python-GIS.html
    - https://pypi.org/project/Shapely/
