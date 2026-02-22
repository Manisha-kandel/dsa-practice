'''
1251. Average Selling Price

The Rule of Thumb: If the prompt asks you to "Return," "Find," or "Report" → Use SELECT.
If the prompt asks you to "Change," "Fix," or "Set" → Use UPDATE
'''
# Write your MySQL query statement below
-- SFW GHO
-- SELECT
-- FROM    (JOIN)
-- WHERE
-- GROUP BY
-- HAVING
-- ORDER BY

-- IN BETWEEN

-- UnitsSold has duplicate rows

-- '''
-- changing the data vs reporting on it: 
-- '''
 
SELECT p.product_id, 
    IFNULL(ROUND(SUM(u.units * p.price) / SUM(u.units), 2), 0) AS average_price
FROM Prices p
LEFT JOIN UnitsSold u ON
    u.product_id = p.product_id AND 
    u.purchase_date BETWEEN p.start_date AND p.end_date
GROUP BY p.product_id