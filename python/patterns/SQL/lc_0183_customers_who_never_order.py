# Write your MySQL query statement below
# Write your MySQL query statement below

-- SELECT
-- FROM
-- WHERE
-- GROUP BY
-- HAVING 
-- ORDER BY

SELECT c.name as Customers
FROM Customers c
LEFT JOIN Orders o
ON c.id = o.customerId
WHERE o.id IS NULL;

-- another soln
-- SELECT c.name as Customers
-- FROM Customers c
-- LEFT JOIN Orders o
-- ON c.id = o.customerId
-- WHERE c.id NOT IN 

-- (SELECT c.id
-- FROM Customers c
-- INNER JOIN Orders o
-- ON c.id = o.customerId);