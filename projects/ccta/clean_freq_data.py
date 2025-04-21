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

mcf_df.head()


# %%

mcf_df = mcf_df.loc[mcf_df.eng.notna()]

# %%

mcf_df = mcf_df.reset_index(drop=True)


# %%

mcf_df

# %%

replace_character = '0xFFD'
print(chr(int(replace_character, base=16)))

test_error_character = chr(int(replace_character, base=16))

# %%

# mcf_df.to_csv('modern_characters_freq_cleaned.csv', sep='\t', index= False, encoding= 'utf-8')
# mcf_df.hanzi.to_csv('simplified_hanzi.csv', index=False, header=False)

# %%

trad_hanzi = pd.read_csv('traditional_hanzi.csv', 
                         names= ['traditional'],
                         encoding= 'utf-8',
                         skip_blank_lines= False)

# %%

# has NA values
trad_hanzi.isna().sum()

# %%

# get index where NA
idx = trad_hanzi.loc[trad_hanzi.traditional.isna()].index

# %%

# fill in missing values at index
missing_charaters = ['孀', '菀', '碭', '貲', '籀','駘']
trad_hanzi.loc[idx, 'traditional'] = missing_charaters

# %%

trad_hanzi.to_csv('traditional_hanzi_1.csv', header= False, index= False, encoding= 'utf-8')

# %%

mcf_df.insert(1, 'traditional', trad_hanzi)

# %%

mcf_df.isna().sum(axis=0)

# %%

mcf_df.rename(columns= {'hanzi':'simplified'}, inplace=True)

# %%

mcf_df

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

import re

# %%

ccre = re.compile(r'\[(.*)\]')

res = ccre.search('䰾魚 鲃鱼 [ba1 yu2] /barbel (fish)/')

print(res)

# %%

ccre = re.compile(r'\[(.*)\]')

res = ccre.search('㐜 㐜 [chou2] /variant of 仇[chou2]/')

print(res)



# %%

ccre = re.compile(r'(.+)\s(.+)\s\[(.+)\]\s/(.+)/')

res = ccre.search('11區 11区 [Shi2 yi1 Qu1] /(ACG) Japan (from the anime "Code Geass", in which Japan was renamed Area 11)/test/test/')

print(res.groups())

# %%

for m in res.groups():
    print(m)

# %%

new_df = pd.DataFrame(columns=['traditional', 'simplified', 'pinyin', 'eng'])

# %%

s_group = pd.Series(res.groups())
s_group.index = new_df.columns
s_group.to_frame().T

# %%

pd.concat([new_df, s_group.to_frame().T], axis= 0, ignore_index=True)

# %%

new_df.loc[0] = s_group

# %%
new_df
# %%

with open(os.path.join(path_to_vocab, 'cc-cedict.u8'), encoding='utf-8', mode='r') as file:
    ccdict = file.read()
    
# %%

cclist = ccdict.split('\n')

# %%

ccprep = [line for line in cclist if line[0] != '#']

# %%

ccre = re.compile(r'(.+)\s(.+)\s\[(.+)\]\s/(.+)/')

res = ccre.search(ccprep[101])

print(res.groups())

# %%

ccfinish = []
for entry in ccprep:
    result = ccre.search(entry)
    ccfinish.append(result.groups())
    
# %%

cc_df = pd.DataFrame(ccfinish, columns= ['traditional', 'simplified', 'pinyin', 'eng'])

# %%

cc_df.isna().apply(sum, 0)

# %%

hsk_df = pd.read_csv('chinese_vocabulary_lists/words/hsk1-6.csv', sep='\t', usecols= [0,2,3,4])
hsk_df

# %%

hsk_df.shape

# %%

inter_hsk_cc = np.intersect1d(cc_df.simplified, hsk_df.Hanzi)

# %%

diff_hsk_cc = np.setdiff1d(hsk_df.Hanzi, inter_hsk_cc)

# %%

hsk_df.loc[hsk_df.Hanzi.isin(diff_hsk_cc)]

# %%

