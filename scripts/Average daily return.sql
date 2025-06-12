-- SELECT * FROM new_schema.stock_data;

-- Top 3 stocks by overall return
SELECT Ticker,
       (MAX(Close) - MIN(Close)) / MIN(Close) * 100 AS ReturnPercent
FROM stock_data
GROUP BY Ticker
ORDER BY ReturnPercent DESC
LIMIT 3;

-- Average daily return for each stock
SELECT Ticker,
       AVG((Close - Open) / Open * 100) AS Avg_Daily_Return
FROM stock_data
GROUP BY Ticker;
