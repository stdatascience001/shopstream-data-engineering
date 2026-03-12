SELECT
    product_id,
    product_name,
    category,
    price,
    stock_quantity
FROM {{ ref('stg_products') }}
