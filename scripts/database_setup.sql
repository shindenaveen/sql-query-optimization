CREATE TABLE sales (
    order_id INT,
    customer_id INT,
    order_date DATE,
    product_id INT,
    quantity INT,
    price DECIMAL(10,2)
);

-- Load CSV data here using your preferred method or copy-paste insert statements below

INSERT INTO sales VALUES 
(1,1001,'2024-01-01',2001,3,100),
(2,1002,'2024-01-02',2003,5,50),
(3,1001,'2024-01-03',2002,2,150),
(4,1003,'2024-01-04',2001,1,100),
(5,1004,'2024-01-05',2004,7,30);
