USE sakila;

-- 1
SELECT * FROM customer WHERE first_name LIKE 'J%' AND active = 1;

-- 2
SELECT * FROM film WHERE title LIKE '%ACTION%' OR description LIKE '%WAR%';

-- 3
SELECT * FROM customer WHERE last_name <> 'SMITH' AND first_name LIKE '%a';

-- 4
SELECT * FROM film WHERE rental_rate > 3.0 AND replacement_cost IS NOT NULL;

-- 5
SELECT store_id, COUNT(*) AS active_customers FROM customer WHERE active = 1 GROUP BY store_id;

-- 6
SELECT DISTINCT rating FROM film;

-- 7
SELECT rental_duration, COUNT(*) AS films FROM film GROUP BY rental_duration HAVING AVG(length) > 100;

-- 8
SELECT DATE(payment_date) AS pay_date, SUM(amount) AS total FROM payment GROUP BY pay_date HAVING COUNT(*) > 100;

-- 9
SELECT * FROM customer WHERE email IS NULL OR email LIKE '%.org';

-- 10
SELECT * FROM film WHERE rating IN ('PG', 'G') ORDER BY rental_rate DESC;

-- 11
SELECT length, COUNT(*) AS films FROM film WHERE title LIKE 'T%' GROUP BY length HAVING COUNT(*) > 5;

-- 12
SELECT actor_id, COUNT(*) AS films FROM film_actor GROUP BY actor_id HAVING COUNT(*) > 10;

-- 13
SELECT title, rental_rate, length FROM film ORDER BY rental_rate DESC, length DESC LIMIT 5;

-- 14
SELECT c.customer_id, c.first_name, COUNT(r.rental_id) AS rentals FROM customer c LEFT JOIN rental r USING (customer_id) GROUP BY c.customer_id ORDER BY rentals DESC;

-- 15
SELECT title FROM film WHERE film_id NOT IN (SELECT i.film_id FROM inventory i JOIN rental r USING (inventory_id));
