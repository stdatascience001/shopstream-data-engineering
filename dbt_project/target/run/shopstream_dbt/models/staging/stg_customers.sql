
  
  create view "shopstream"."main"."stg_customers__dbt_tmp" as (
    with source as (
    select * from 'd:/shopstream/data/bronze/customers.csv'
)
select
    customer_id,
    name as full_name,
    email,
    city,
    country,
    signup_date
from source
  );
