# Setting up PostgreSQL, PostGIS, and pgrouting 

# Exercise 1: Help Santa Deliver to Children in Different Countries
### https://blog.daftcode.pl/help-santa-with-the-power-of-postgis-9b8dc8ae73f7

# Exercise 2: Use pgrouting to create network topography
### https://blog.daftcode.pl/find-your-way-with-the-power-of-postgis-pgrouting-66d620ef201b


# Troubleshooting pgrouting installation:
  1. Issue: $libdir not pointing to the right place
  
    - Help:
      - https://www.pg-forum.de/viewtopic.php?t=3357 
      - https://www.postgresql.org/docs/9.5/static/install-post.html
      - https://gis.stackexchange.com/questions/52458/how-to-solve-could-not-access-file-libdir-librouting-problem-in-ubuntu-12-0?rq=1
      - https://github.com/pgRouting/pgrouting/issues/68 : use otool -L to find shared libraries of file
      - http://osgeo-org.1560.x6.nabble.com/pgrouting-users-routing-dd-sql-error-inserting-on-OS-X-Homebrew-td5199424.html
      - https://github.com/pgRouting/pgrouting/issues/290
      
  2. Solution
  
    - In the end, I needed to move the 
    `libpgrouting-2.6.so, pgrouting.control, and pgrouting--2.6.0.sql`
    files to /Applications/Postgres.app/Contents/Versions/10/share/postgresql/extension/ 
    and change the $libdir/libpgrouting variable in the .sql file to the full path. 
    Homebrew's pgrouting doesn't install to the Postgress.App.
    
# Troubleshooting create topology

1. Issue: PGR ERROR in pgr_createTopology: Column source not found when trying: https://blog.daftcode.pl/find-your-way-with-the-power-of-postgis-pgrouting-66d620ef201b

  - Help: 
    - https://docs.pgrouting.org/2.2/en/src/topology/doc/pgr_createTopology.html
    
2. Columns needed to be created:
  - ALTER TABLE roads ADD COLUMN source integer;
  - ALTER TABLE roads ADD COLUMN target integer;
  - CREATE INDEX roads_source_idx ON roads (source);
  - CREATE INDEX roads_target_idx ON roads (target);
