SELECT COUNT(*) AS valid_products
FROM products;

SELECT category,  COUNT(*) AS products_count
FROM products
GROUP BY category;

SELECT TOP 5 manufacturer,  COUNT(*) AS valid
FROM products
GROUP BY manufacturer
ORDER BY valid;

SELECT product_name, unit_price_gbp
FROM products
WHERE currency = 'GBP'
ORDER BY unit_price_gbp DESC;

SELECT product_name, lead_time_days
FROM products
WHERE lead_time_days > 25;




