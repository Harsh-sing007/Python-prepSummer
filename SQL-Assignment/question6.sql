SELECT
    R.RestaurantName,
    SUM(O.BillAmount) AS TotalRevenue
FROM Restaurants R
JOIN Orders O
    ON R.RestaurantID = O.RestaurantID
JOIN Users U
    ON O.UserID = U.UserID
WHERE U.City = 'Delhi'
GROUP BY R.RestaurantID, R.RestaurantName
HAVING SUM(O.BillAmount) > 5000;