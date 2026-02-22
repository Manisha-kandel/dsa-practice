'''
586. Customer Placing the Largest Number of Orders
'''
# Write your MySQL query statement below
-- SELECT
-- FROM
-- WHERE
-- GROUP BY
-- HAVING
-- ORDER BY ... ASC;


SELECT customer_number
FROM Orders
GROUP BY customer_number
ORDER BY COUNT(*) DESC
LIMIT 1;