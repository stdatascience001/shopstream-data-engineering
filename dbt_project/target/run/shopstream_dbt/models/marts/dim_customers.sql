
  
    
    

    create  table
      "shopstream"."main"."dim_customers__dbt_tmp"
  
    as (
      SELECT
    customer_id,
    full_name,
    email,
    city,
    country,
    signup_date
FROM "shopstream"."main"."stg_customers"
    );
  
  