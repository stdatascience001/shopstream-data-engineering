with source as (
    select * from 'd:/shopstream/data/bronze/products.csv'
)
select
    product_id,
    brand as product_name,
    category,
    price,
    10 as stock_quantity
from source