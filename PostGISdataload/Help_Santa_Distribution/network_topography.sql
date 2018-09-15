/* download: https://www.dropbox.com/s/bu9k0k9yfb4ktw3/roads.sql.gz
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
