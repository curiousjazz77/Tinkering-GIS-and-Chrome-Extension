/* SOURCE: https://blog.daftcode.pl/find-your-way-with-the-power-of-postgis-pgrouting-66d620ef201b
* download: https://www.dropbox.com/s/bu9k0k9yfb4ktw3/roads.sql.gz
* gunzip -c roads.sql.gz | psql pgr_tutorial
* The above command creates one table from the dataset:
* CREATE TABLE roads (
*    id integer NOT NULL PRIMARY KEY,
*    geom geometry(LineString, 4326)
*);
*/

//Start with adding two additional columns to our roads table.

ALTER TABLE roads ADD COLUMN source integer;
ALTER TABLE roads ADD COLUMN target integer;
CREATE INDEX roads_source_idx ON roads (source);
CREATE INDEX roads_target_idx ON roads (target);

/* And then use pgr_createTopology function which builds a network topology 
* based on the geometry information (it analyses roads geometry and automatically 
* assigns node ids to the source and target columns).
*/

SELECT pgr_createTopology('roads', 0.0001, 'geom', 'id'); 

/* After about 5 minutes of calculations the dataset will be ready. */

/* Start navigating! 🚗💨
* After this short introduction let’s move to some real-world 
* examples and find the shortest path between nodes #1 
* and #5000 using Dijkstra algorithm.
*/

SELECT seq, node, edge, cost as cost, agg_cost, geom
FROM pgr_dijkstra(
   'SELECT id, source, target, st_length(geom, true) as cost FROM roads',
   1,
   5000
) as pt
JOIN roads rd ON pt.edge = rd.id;
