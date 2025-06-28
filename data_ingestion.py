import yfinance as yf

def fetch_stock_data(ticker, period='6mo', interval='1d'):
    stock = yf.Ticker(ticker)
    data = stock.history(period=period, interval=interval)
    data.dropna(inplace=True)
    return data