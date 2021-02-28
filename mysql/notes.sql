!-- How to add a column at a specific position to a table ?
Alter table customers
ADD column gender ENUM(‘M’,‘F’) after last_name;

!-- Also, for adding a column at the starting position, we can use the specifier ‘FIRST’.
ALTER TABLE customers
ADD COLUMN full_name TEXT FIRST;

!-- delete a specific number of rows?
DELETE FROM customers
WHERE twitter_handle IS NULL
LIMIT 5;

!-- When searching for a pattern containing the specific characters % or _, we can utilize the escape character \, similarly to its use in Python.
SELECT * FROM books WHERE title LIKE '% 100\%';

!-- What is the max chars for each type of data in sql ??
!-- e.g Numeric: bit, tinyint, smallint, int, bigint, decimal, numeric, float, real
!-- Date/Time: Date, Time, Datetime, Timestamp and year
!-- Character String: Char, Varchar, Varchar(Max), Text.
!-- Unicode Character/String : Nchar, NVarchar, NVarchar(max), NText
!-- Binary: Binary, Varbinary, Varbinary(max), image
!-- Miscellaneous: Clob, Blob, XML, JSON




