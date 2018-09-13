#Correction to article: https://blog.daftcode.pl/help-santa-with-the-power-of-postgis-9b8dc8ae73f7
SELECT name FROM countries WHERE ST_Within( ST_SetSRID(ST_MakePoint(-64.504169, -15.953918), 4326), geom );
