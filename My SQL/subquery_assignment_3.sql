USE sakila;

-- 1
SELECT * FROM customer
WHERE customer_id IN (SELECT customer_id FROM payment GROUP BY customer_id HAVING COUNT(*) > 5);

-- 2
SELECT first_name, last_name FROM actor
WHERE actor_id IN (SELECT actor_id FROM film_actor GROUP BY actor_id HAVING COUNT(*) > 10);

-- 3
SELECT first_name, last_name FROM customer
WHERE customer_id NOT IN (SELECT customer_id FROM payment);

-- 4
SELECT * FROM film
WHERE rental_rate > (SELECT AVG(rental_rate) FROM film);

-- 5
SELECT title FROM film
WHERE film_id NOT IN (
  SELECT i.film_id FROM inventory i JOIN rental r ON i.inventory_id = r.inventory_id
);

-- 6
SELECT DISTINCT c.* FROM customer c
JOIN rental r ON c.customer_id = r.customer_id
WHERE DATE_FORMAT(r.rental_date, '%Y-%m') IN (
  SELECT DATE_FORMAT(rental_date, '%Y-%m') FROM rental WHERE customer_id = 5
) AND c.customer_id <> 5;

-- 7
SELECT * FROM staff
WHERE staff_id IN (
  SELECT staff_id FROM payment WHERE amount > (SELECT AVG(amount) FROM payment)
);

-- 8
SELECT title, rental_duration FROM film
WHERE rental_duration > (SELECT AVG(rental_duration) FROM film);

-- 9
SELECT * FROM customer
WHERE address_id = (SELECT address_id FROM customer WHERE customer_id = 1)
  AND customer_id <> 1;

-- 10
SELECT * FROM payment
WHERE amount > (SELECT AVG(amount) FROM payment);
