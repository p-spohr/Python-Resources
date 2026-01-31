import numpy as np
import pandas as pd

rng = np.random.default_rng()

test_ret = rng.normal(0,1,(20,3))

test_df = pd.DataFrame(test_ret, columns= ['A', 'B', 'C'])



stock_country = {'A': 'USA', 'B': 'GER', 'C': 'JPN'}
(
    pd.melt(test_df, value_vars= test_df.columns, var_name= 'stock', value_name= 'returns').
    assign(country= lambda x: [stock_country[stock_name] for stock_name in x.stock]).
    pivot(columns= ['stock', 'country'], values= ['returns'])
)