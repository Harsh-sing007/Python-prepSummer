SELECT
    O.OrderID,
    U.UserName
FROM Users U
JOIN Orders O
    ON U.UserID = O.UserID
JOIN Deliveries D
    ON O.OrderID = D.OrderID
WHERE D.DeliveryTime > 35;