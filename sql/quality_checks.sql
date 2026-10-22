
SELECT COUNT(*) AS total_rows
FROM cleaned_sales;

SELECT order_id, COUNT(*)
FROM cleaned_sales
GROUP BY order_id
HAVING COUNT(*) > 1;

SELECT SUM(total_amount) AS total_revenue
FROM cleaned_sales;

SELECT city, SUM(total_amount) AS revenue
FROM cleaned_sales
GROUP BY city
ORDER BY revenue DESC;

SELECT *
FROM cleaned_sales
WHERE quantity <= 0 OR unit_price <= 0;
