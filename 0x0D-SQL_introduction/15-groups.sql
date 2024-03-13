-- SQL command to list records with same score.
-- Order records in desc count.
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
