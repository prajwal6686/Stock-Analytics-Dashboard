# 📊 Stock Analytics Dashboard using Python + SQL + Power BI

This project is a full data pipeline that showcases stock market data extraction, storage, analysis, and visualization using a modern tech stack:

- ✅ Python (`yfinance`) for data download
- ✅ SQLite/MySQL for data storage
- ✅ SQL for analytics (e.g., top-performing stocks, average returns)
- ✅ Power BI for dynamic visual dashboards

---

## 🚀 Project Steps

1. **Download Data**  
   Used `yfinance` to download historical data of selected NIFTY 50 stocks.

2. **Store in SQL**  
   Pushed the data into SQLite (can be switched to MySQL). Tables include daily OHLCV data.

3. **Query the Data**  
   Wrote SQL queries to find:
   - Top-performing stocks by return %
   - Average daily return
   - Volatility (standard deviation)
   - Volume comparisons

4. **Visualize in Power BI**  
   Built a Power BI dashboard with:
   - Trend line chart of stock prices
   - Stacked column chart for daily volume
   - KPI cards for returns
   - Sector-wise or stock-wise filters

---

## 📷 Screenshots
*(Add your actual screenshots below)*

| Dashboard Overview | SQL Data View |
|--------------------|---------------|
| ![Dashboard](screenshots/dashboard.png) | ![SQL](screenshots/sql_data.png) |

---

## 📁 Files Included
- `data_download.py` – Python script to pull stock data from Yahoo Finance  
- `store_to_sql.py` – Store the data in SQL (SQLite or MySQL)  
- `stock_queries.sql` – SQL queries for analysis  
- `dashboard.pbix` – Power BI Dashboard file  
- `/screenshots/` – Dashboard screenshots  

---

## 📌 Requirements

- Python 3.x
  - `pandas`
  - `yfinance`
  - `SQLAlchemy` (or `sqlite3` for SQLite)
- SQLite or MySQL
- Power BI Desktop

---

## 🧠 Learnings

- How to automate stock data ingestion
- Store large data efficiently in SQL
- Build analytical dashboards with real-time insights
- Connect SQL database directly to Power BI

---

## 🙋‍♂️ Author

**Prajwal Aughade**  
📧 [Prajwalaughade123@gmail.com]  
🔗 [https://www.linkedin.com/in/prajwal-aughade/]

---

## 🗂️ License

This project is open source under the MIT License.
