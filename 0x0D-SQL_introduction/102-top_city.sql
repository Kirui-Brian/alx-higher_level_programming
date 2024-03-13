-- SQL command to display 3 cities with highest avg.
-- Temp between July & Aug.
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month = 7 OR month = 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
