
  
    
    

    create  table
      "shopstream"."main"."dim_products__dbt_tmp"
  
    as (
      SELECT
    product_id,
    product_name,
    category,
    price,
    stock_quantity
FROM "shopstream"."main"."stg_products"
    );
  
  