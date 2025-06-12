import yfinance as yf
import pandas as pd

# Define list of stock tickers
tickers = ['INFY.NS', 'HDFCBANK.NS', 'RELIANCE.NS']

# Download historical data
data = yf.download(tickers, start="2022-01-01", end="2025-06-10", group_by='ticker')

# Flatten MultiIndex columns
flat_data = []
for ticker in tickers:
    df = data[ticker].copy()
    df['Ticker'] = ticker
    df = df.reset_index()
    flat_data.append(df)

combined_df = pd.concat(flat_data)
combined_df.reset_index(drop=True, inplace=True)

# Preview
print(combined_df.head())

# Save to CSV for next step
combined_df.to_csv('stock_data.csv', index=False)
