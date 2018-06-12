SELECT Name AS Customers
FROM Customers
LEFT JOIN Orders ON Customers.Id = Orders.CustomerId
WHERE Orders.Id IS NULL;

-- OR

SELECT Name AS Customers
FROM Customers
WHERE Id NOT IN (
    SELECT CustomerId
    FROM Orders
);
