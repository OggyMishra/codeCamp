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

