SELECT
    o.order_id,
    o.order_date,
    o.order_amount,
    o.order_status,
    c.customer_id,
    c.country AS customer_country,
    p.category AS product_category
FROM "shopstream"."main"."stg_orders" o
LEFT JOIN "shopstream"."main"."dim_customers" c USING (customer_id)
LEFT JOIN "shopstream"."main"."dim_products" p USING (product_id)