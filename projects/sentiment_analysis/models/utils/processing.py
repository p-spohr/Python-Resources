# functions for preparing data
from pandas import Series
from yfinance import Ticker
from datetime import date
from pathlib import Path
import numpy as np

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

def simulate_stock_price(mean, sigma, t_delta, size, S0) -> tuple[np.ndarray, np.ndarray]:
    '''
    Simulate a stock price path using geometric brownian motion.
    '''
        
    np_rng = np.random.default_rng()
    
    # drift term
    drift = mean + 0.5 * np.pow(sigma, 2)
    
    gbb = np.array([S0])
    
    for i in range(0,(size - 1)):
        St = gbb[i] * np.exp( drift * t_delta + sigma * np.sqrt(t_delta) * np_rng.normal() )
        gbb = np.append(gbb, St)

    x_axis = np.arange(0, size * t_delta, t_delta)
    
    return x_axis, gbb

def numpy_sequence_target(time_series : np.array, sequence_length: int) -> tuple[np.array, np.array]:
    sequence = None
    targets = None
    for i in range(0, len(time_series) - sequence_length):
        seq_test = time_series[i:i + sequence_length]
        if seq_test.size == sequence_length:
            seq = np.resize(time_series[i:i + sequence_length], (1, sequence_length, 1))
            if sequence is None:
                sequence = seq
            else:
                sequence = np.vstack((sequence, seq))
                
            targ = time_series[i + sequence_length]
            if targets is None:
                targets = targ
            else:
                targets = np.append(targets, targ)
                
    return sequence, targets