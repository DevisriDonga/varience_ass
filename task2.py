import yfinance as yf
import pandas as pd
import pandas_ta as ta

class FinanceDataHandler:
    def process_ticker_data(self, ticker):
        data = yf.download(ticker)  # Download data
        data = data.round(2)  # Round all columns to 2 decimal places
        data.columns = data.columns.str.lower()  # Convert column names to lower case
        data['color'] = ['GREEN' if open <= close else 'RED' for open, close in zip(data['open'], data['close'])]
        data['EMA'] = ta.ema(data['close'], length=9)  # Calculate EMA and add as a column
        data.to_csv(f'{ticker}.csv', index=False)  # Save to CSV

# Usage example:
# Instantiate FinanceDataHandler
handler = FinanceDataHandler()
# Process data for a specific ticker
handler.process_ticker_data('AAPL')