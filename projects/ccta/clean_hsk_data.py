# %%

import pandas as pd
import numpy as np
import os

# %%

path_to_file = 'chinese_vocabulary_lists/raw/hsk1-6.csv'

# %%

chn_df = pd.read_csv(path_to_file,
                     skiprows=7, 
                     delimiter='\t',
                     encoding= 'utf-8',
                     names= ['level', 'word', 'pinyin', 'eng'],
                     usecols= [0,2,3,4])

# %%
    
chn_df.head(n=5)

# %%

save_to_file = 'chinese_vocabulary_lists/cleaned/hsk1-6_cleaned.csv'

# %%

chn_df.to_csv(save_to_file,
              sep= '\t',
              encoding= 'utf-8',
              index= False)

# %%
