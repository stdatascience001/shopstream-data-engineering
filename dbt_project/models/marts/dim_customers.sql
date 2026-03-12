SELECT
    customer_id,
    full_name,
    email,
    city,
    country,
    signup_date
FROM {{ ref('stg_customers') }}
