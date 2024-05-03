import yfinance as yf
import pandas as pd
import pandas_ta as ta

class FinanceDataHandler:
    def process_ticker_data(self, ticker):
        data = yf.download(ticker)
        data = data.round(2)
        data.columns = data.columns.str.lower()
        data['color'] = ['GREEN' if open <= close else 'RED' for open, close in zip(data['open'], data['close'])]
        data['EMA'] = ta.ema(data['close'], length=9)
        data.to_csv(f'{ticker}.csv', index=False)
