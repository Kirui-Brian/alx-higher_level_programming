-- SQL command to display the avg temp (in Fahrenheit).
-- by city ordered by desc temp.
SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
