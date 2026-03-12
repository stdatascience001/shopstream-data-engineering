SELECT
    order_id,
    customer_id,
    product_id,
    CAST(quantity AS INTEGER) AS quantity,
    CAST(amount AS DECIMAL(10,2)) AS order_amount,
    CAST(order_date AS DATE) AS order_date,
    UPPER(status) AS order_status
FROM 'd:/shopstream/data/bronze/orders.csv'
WHERE order_id IS NOT NULL
    AND amount > 0