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

def pos_neg_sum(ser_data : pd.Series):
    temp_sum = ser_data.loc['positive'] + ser_data.loc['negative']
    news_sum = ser_data.loc['news_volume']
    company = ser_data.loc['company']
    return pd.Series(
        {
            'company': company,
            'sentiment_summed': temp_sum,
            'news_summed': news_sum
        }
    )

# %%
(
    sent_df
    .loc[:, ['company', 'positive', 'negative', 'news_volume']]
    .apply(pos_neg_sum, axis=1)
)

# %%

target_comp_list = (
    sent_df
    .filter(['date', 'company'])
    .groupby(by='company')
    .count()
    .query("date ==394")
    .index
    .values

)


# %%

target_comp_list


# %%

sent_df_3 = sent_df[sent_df.company.isin(target_comp_list)]

# %%
(   
    sent_df_3
    .groupby('company')
    .news_volume
    .mean()
    .to_frame(name='mean_news_volume')
    .sort_values(by='mean_news_volume', ascending=True)
    .query('mean_news_volume > 100')
    .to_csv('potential_companies_by_news_volume.csv')
)

# %%

chevron_df = sent_df.query('company =="chevron"')

# %%
