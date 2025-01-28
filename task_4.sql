-- task_4.sql
SELECT 
    COLUMN_NAME AS `Field`,
    CONCAT(DATA_TYPE,
        IF(CHARACTER_MAXIMUM_LENGTH IS NOT NULL, 
            CONCAT('(', CHARACTER_MAXIMUM_LENGTH, ')'), 
            IF(DATA_TYPE = 'decimal', 
                CONCAT('(', NUMERIC_PRECISION, ',', NUMERIC_SCALE, ')'), 
                '')
        )
    ) AS `Type`,
    IS_NULLABLE AS `Null`,
    COLUMN_KEY AS `Key`,
    COLUMN_DEFAULT AS `Default`,
    EXTRA AS `Extra`
FROM information_schema.columns
WHERE TABLE_SCHEMA = DATABASE() AND TABLE_NAME = 'Books'
ORDER BY ORDINAL_POSITION;
