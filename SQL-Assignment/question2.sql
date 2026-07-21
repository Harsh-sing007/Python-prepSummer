
SELECT DISTINCT
    R.RestaurantName
FROM Restaurants R
JOIN Orders O
    ON R.RestaurantID = O.RestaurantID;