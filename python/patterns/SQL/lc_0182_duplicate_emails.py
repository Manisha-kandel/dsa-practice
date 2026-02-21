# Write your MySQL query statement below

-- SELECT
-- FROM
-- WHERE
-- GROUP BY
-- HAVING 
-- ORDER BY

SELECT p.email 
FROM Person p
GROUP BY email
HAVING COUNT(email) > 1;