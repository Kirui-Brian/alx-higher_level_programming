-- SQL command to list records having same value.
-- Order by desc score.
SELECT score, name
FROM second_table
WHERE name !="" -- IS NOT NULL (is also valid).
ORDER BY score DESC;
