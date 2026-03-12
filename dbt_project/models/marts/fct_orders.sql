SELECT
    o.order_id,
    o.order_date,
    o.order_amount,
    o.order_status,
    c.customer_id,
    c.country AS customer_country,
    p.category AS product_category
FROM {{ ref('stg_orders') }} o
LEFT JOIN {{ ref('dim_customers') }} c USING (customer_id)
LEFT JOIN {{ ref('dim_products') }} p USING (product_id)
