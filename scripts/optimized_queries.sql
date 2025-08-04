-- Add index for faster group by on product_id
CREATE INDEX idx_product_id ON sales(product_id);

-- Optionally, use a stored procedure to encapsulate repeated analysis

CREATE PROCEDURE GetSalesSummary()
BEGIN
  SELECT product_id,
         SUM(quantity) AS total_quantity,
         SUM(quantity * price) AS total_revenue
  FROM sales
  GROUP BY product_id;
END;
