-- Script that lists all records of the table second_table
-- Display both the score and the name
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
