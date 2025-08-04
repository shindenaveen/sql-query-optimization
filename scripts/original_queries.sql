-- Count total quantity sold and total revenue per product without indexes or aggregation optimization

SELECT product_id,
       SUM(quantity) AS total_quantity,
       SUM(quantity * price) AS total_revenue
FROM sales
GROUP BY product_id;
