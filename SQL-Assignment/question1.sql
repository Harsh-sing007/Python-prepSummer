SELECT
    U.UserName,
    R.RestaurantName,
    O.BillAmount
FROM Users U
JOIN Orders O
    ON U.UserID = O.UserID
JOIN Restaurants R
    ON O.RestaurantID = R.RestaurantID;