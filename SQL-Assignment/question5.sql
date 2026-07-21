SELECT
    U.UserName,
    COUNT(O.OrderID) AS TotalOrders
FROM Users U
LEFT JOIN Orders O
    ON U.UserID = O.UserID
GROUP BY U.UserID, U.UserName;