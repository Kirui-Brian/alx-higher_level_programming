USE $1;

SELECT CONCAT('Table   Create Table'),
       CONCAT(TABLE_NAME, '     ', CREATE_TABLE) AS 'Create Table'
FROM information_schema.TABLES
WHERE TABLE_SCHEMA = DATABASE() AND TABLE_NAME = 'first_table';
