# %%

import pandas as pd
import numpy as np
import os

# %%

path_to_file = 'chinese_vocabulary_lists/raw'

# %%

mcf_df = pd.read_table(os.path.join(path_to_file, 'modern_character_freq.txt'), 
              encoding= 'gb2312', 
              delimiter='\t',
              skiprows= 5,
            #   nrows= 5,
              encoding_errors='replace',
              index_col= False,
              usecols= [1,2,4,5],
              header= 0,
              names = ['hanzi', 'freq', 'pinyin', 'eng'])

# %%

mcf_df

# %%

mcf_df.loc[mcf_df.hanzi == '啰']

# %%

replace_character = hex(ord('�'))

# %%

mcf_df.hanzi

# %%

def replace_error(data_ser : pd.Series, rep_char : str):
  char_list = list(data_ser)
  error_check = False
  for char in char_list:
    if hex(ord(char)) == rep_char:
      error_check = True

  return error_check

# %%

error_ser = mcf_df.hanzi.apply(replace_error, args= (replace_character,))

# %%

mcf_df = mcf_df.assign(error=error_ser)

# %%

mcf_df = mcf_df.loc[mcf_df.error != True]

# %%

mcf_df = mcf_df.reset_index(drop=True)

# %%

mcf_df

# %%

# mcf_df.to_csv('modern_characters_freq_cleaned.csv', sep='\t', index= False, encoding= 'utf-8')
# mcf_df.hanzi.to_csv('simplified_hanzi.csv', index=False, header=False)

# %%

trad_hanzi = pd.read_csv('traditional_hanzi.csv', 
                         names= ['traditional'],
                         encoding= 'utf-8',
                         skip_blank_lines= False)

# %%

combined_df = pd.DataFrame({'simplified': mcf_df.hanzi,
              'traditional': trad_hanzi.traditional})

# %%

combined_df.loc[combined_df.traditional.isna()]

# %%

# get index where NA
idx = combined_df.loc[combined_df.traditional.isna()].index

# %%

# fill in missing values at index
missing_charaters = ['孀', '菀', '碭', np.nan, '貲', '籀','駘', np.nan]
combined_df.loc[idx, 'traditional'] = missing_charaters

# %%

combined_df = combined_df.loc[combined_df.traditional.notna()]

# %%

mcf_df = mcf_df.rename(columns= {'hanzi': 'simplified'})

# %%

mcf_df = mcf_df.merge(combined_df, how='left', on='simplified')

# %%

mcf_df.isna().sum(axis=0)

# %%

mcf_df.rename(columns= {'hanzi':'simplified'}, inplace=True)

# %%

mcf_df = mcf_df.loc[mcf_df.traditional.notna()]

# %%

mcf_df = mcf_df[['simplified', 'traditional', 'pinyin', 'eng', 'freq']]

# %%

mcf_df.to_csv('modern_characters_freq_cleaned.csv',
              encoding= 'utf-8',
              index= False,
              sep= '\t')

# %%

# mcf_df.to_csv('modern_characters_freq_cleaned.csv', sep= '\t', encoding= 'utf-8', index= False)


# %%

hsk_df = pd.read_csv('chinese_vocabulary_lists/cleaned/hsk1-6_cleaned.csv',
                     sep= '\t',
                     encoding= 'utf-8')

# %%

mcf_df.loc[mcf_df.simplified == hsk_df.loc[0, 'word']]

# %%

# NEEDS EDITING AND ORGANIZING
fbf_df = pd.read_table(os.path.join(path_to_vocab, 'fiction_bigram_freq.txt'),
              encoding= 'gb2312',
              delimiter= '\t',
            #   nrows=5,
              skiprows=2,
              usecols= [1,2,3],
              names= ['word', 'freq', 'mutual'],
              encoding_errors='replace')

# %%

fbf_df

# %%

nbf_df = pd.read_table(os.path.join(path_to_vocab, 'nonfiction_bigram_freq.txt'),
              encoding= 'gb2312',
              delimiter= '\t',
            #   nrows=5,
              skiprows=2,
              usecols= [1,2,3],
              names= ['word', 'freq', 'mutual'],
              encoding_errors='replace')

# %%

print(fbf_df.shape)
print(nbf_df.shape)

# %%

fbf_df.word.isin(nbf_df.word).sum()

# %%

np.intersect1d(fbf_df.word, nbf_df.word).size

# %%

pd.read_table(os.path.join(path_to_vocab, 'cc-cedict.u8'),
                          encoding='utf-8',
                          delimiter='\t',
                          nrows=5,
                          skiprows=30)

# %%

ccdict_df = pd.read_table(os.path.join(path_to_vocab, 'cc-cedict.u8'),
                          encoding='utf-8',
                          delimiter='\t',
                          nrows=5)

# %%

