SELECT W1.Id
FROM Weather AS W1, Weather AS W2
WHERE W1.Temperature > W2.Temperature
AND W1.RecordDate = W2.RecordDate + INTERVAL 1 DAY;
