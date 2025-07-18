-- Get full description of the table first_table from information_schema
SELECT COLUMN_NAME, COLUMN_TYPE, IS_NULLABLE, COLUMN_DEFAULT
FROM information_schema.COLUMNS
WHERE table_schema = 'hbtn_0c_0' AND table_name = 'first_table';
