use test;
(SELECT 'id', 'name', 'email' from users)
UNION 
SELECT id, name, email from users
INTO OUTFILE '/Users/Van/projects/scripting_for_DE_python/van.csv'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'

