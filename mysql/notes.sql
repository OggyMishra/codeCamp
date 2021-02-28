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

!-- Calculations performed on multiple rows of a table are called aggregates.
!-- TODO:
!-- When using the SQL COUNT() function for a column, does it include duplicate values?
!-- Yes, when using the COUNT() function on a column in SQL, it will include duplicate values by default. It essentially counts all rows for which there is a value in the column.
!-- If you wanted to count only the unique values in a column, then you can utilize the DISTINCT clause within the COUNT() function.
SELECT COUNT(DISTINCT category)
FROM fake_apps;

--When do we use the COUNT() function or the SUM() function?
--
--Although they might appear to perform a similar task, the COUNT() and SUM() functions have very different uses.
--
-- COUNT() is used to take a name of a column, and counts the number of non-empty values in that column.
-- COUNT() does not take into account the actual values stored, and only cares if they have a non-empty value.
-- Each row is essentially counted as 1 towards the total count.
-- On the other hand, SUM() takes a column name, and returns the sum of all values in the column, meaning that it must take into account the actual values stored.
-- In general, use COUNT() when you want to count how many rows contain a non-empty value for a specified column. Use SUM() when you want to get the total sum of all values in a column.

--
--SQL lets us use column reference(s) in our GROUP BY that will make our lives easier.
--
--    1 is the first column selected
--    2 is the second column selected
--    3 is the third column selected


