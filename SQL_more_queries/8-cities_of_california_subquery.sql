-- Write a script that lists all the cities of California that can be found in the database hbtn_0d_usa. --
-- Get the state_id for California
SET @california_id = (SELECT id FROM states WHERE name = 'California');

-- List all cities of California
SELECT * FROM cities
WHERE state_id = @California_id
ORDER BY id ASC
