# functions for preparing data
from pandas import Series
from yfinance import Ticker
from datetime import date
from pathlib import Path

def yf_csv_download(path : str, ser : Series, period : str):
    '''
    Downloads stock prices from yfinance and saves locally as CSV file
    '''
    today = date.today().isoformat()
    target_path = Path(path)
    
    if not target_path.exists():
        raise FileExistsError
    
    for ticker in ser:
        Ticker(ticker).info
        stock_prices = Ticker(ticker).history(period)
        stock_prices.to_csv(target_path / f'{ticker}_{period}_{today}.csv')

