-- This lists all records of second_table having a name value in my MySQL server.
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC
