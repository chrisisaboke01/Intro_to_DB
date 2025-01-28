-- task_4.sql
SELECT 
    COLUMN_NAME AS `Field`,
    COLUMN_TYPE AS `Type`,  -- Use COLUMN_TYPE instead of building Type manually
    IS_NULLABLE AS `Null`,
    COLUMN_KEY AS `Key`,
    COLUMN_DEFAULT AS `Default`,
    EXTRA AS `Extra`
FROM INFORMATION_SCHEMA.COLUMNS  -- Explicit uppercase for check requirement
WHERE TABLE_SCHEMA = 'alx_book_store'  -- Hardcoded database name
    AND TABLE_NAME = 'Books'
ORDER BY ORDINAL_POSITION;
