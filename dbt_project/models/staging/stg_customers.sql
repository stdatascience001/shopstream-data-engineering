with source as (
    select * from {{ source('bronze', 'customers') }}
)
select
    customer_id,
    name as full_name,
    email,
    city,
    country,
    signup_date
from source
