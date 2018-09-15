/* Source: https://blog.daftcode.pl/help-santa-with-the-power-of-postgis-9b8dc8ae73f7
* Steps: 
* 1. Download and install Postgres.app which comes with build-in PostGIS support.
* 2. Create an empty database and connect to it using psql . 
* $ createdb santa_project
* $ psql santa_project
* 3. Next, enable the PostGIS extension on this newly crated database:
* santa_project=# CREATE EXTENSION postgis;
* Now you are ready to join the Santa Team!
*
* It’s finally time for the real work with our spatial data. 
* To be able to work with PostGIS features you can download the sample data: https://dl.getdropbox.com/s/1op0rrqp6xfwvud/santa_db.sql
* for your database provided by the elves working in the Santa’s North Pole Data Center. 
* To load it use:
* $ psql santa_project < santa_db.sql
*
*
* The script will automatically create the following tables:
* CREATE TABLE countries (
*     id integer NOT NULL PRIMARY KEY,
*     name character varying(256),
*     geom geometry(MultiPolygon, 4326)
* );
* 
* create table capitals (
*     id integer NOT NULL PRIMARY KEY,
*     name character varying(256),
*     geom geometry(Point, 4326)
* );
* 
* CREATE TABLE children (
*     id integer NOT NULL PRIMARY KEY,
*     name character varying(256),
*     geom geometry(Point, 4326)
* );
*/

/* Problem 1: List of countries ordered by their area. */

SELECT name, ST_Area(geom, true) AS area
FROM countries
ORDER BY area DESC;

/* Problem 2: List of 5 countries with the highest number of children. */ 


SELECT countries.name, COUNT(children.id) AS children_count
FROM countries
LEFT JOIN children ON ST_Within(children.geom, countries.geom)
GROUP BY countries.id, countries.name
ORDER BY children_count DESC
LIMIT 5;

/*Problem 3: List of 5 capitals with the highest number of children in 200km radius. */
SELECT capitals.name, COUNT(children.id) AS children_count
FROM capitals
LEFT JOIN children ON
    ST_Distance(children.geom, capitals.geom, true) <= 200000
GROUP BY capitals.id, capitals.name
ORDER BY children_count DESC
LIMIT 5;

/* Problem 4 One of Santa’s secret distribution centers is located in this 
* coordinates: lat -15.953918, lon -64.504169. Let’s find out what country it is.
*/ 
/*Correction to article: https://blog.daftcode.pl/help-santa-with-the-power-of-postgis-9b8dc8ae73f7*/
SELECT name FROM countries WHERE ST_Within( ST_SetSRID(ST_MakePoint(-64.504169, -15.953918), 4326), geom );

/* Problem 5 Now we know where the distribution center is, 
* so we can check which countries border with Bolivia to deliver gifts from there.
*/

SELECT name
FROM countries
WHERE ST_Intersects(
        (SELECT geom FROM countries WHERE name='Bolivia'),
        geom
      )
      AND name != 'Bolivia';

