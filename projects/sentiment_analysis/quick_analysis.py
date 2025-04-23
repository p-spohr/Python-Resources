# %%

import pandas as pd
import numpy as np

# %%

sent_df = pd.read_csv('data/raw/sentiment.csv', sep=',')

# %%

sent_df

# %%

sent_df.company.value_counts()

# %%

sent_df_1 = (
    sent_df
    .loc[:, ['company', 'positive', 'negative']]
    .groupby(['company'])
    .sum()
)

# %%

sent_df_2 = (
    sent_df_1
    .assign(total = sent_df_1.apply(sum, axis=1))
    .sort_values('total', ascending= True)
)

# %%

sent_df.drop(['ISIN', 'date', 'share'], axis= 1).groupby(['company'], axis=0).mean().mean(axis=0)

# %%
