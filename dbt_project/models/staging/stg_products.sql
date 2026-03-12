with source as (
    select * from {{ source('bronze', 'products') }}
)
select
    product_id,
    brand as product_name,
    category,
    price,
    10 as stock_quantity
from source
