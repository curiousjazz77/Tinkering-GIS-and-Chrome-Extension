/*download: https://www.dropbox.com/s/bu9k0k9yfb4ktw3/roads.sql.gz
* gunzip -c roads.sql.gz | psql pgr_tutorial
* The above command creates one table from the dataset:
* CREATE TABLE roads (
*    id integer NOT NULL PRIMARY KEY,
*    geom geometry(LineString, 4326)
*);
*/

