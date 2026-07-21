SELECT
    U.UserName,
    SUM(O.BillAmount) AS TotalSpend
FROM Users U
JOIN Orders O
    ON U.UserID = O.UserID
GROUP BY U.UserName;
