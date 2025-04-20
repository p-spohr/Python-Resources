# %%

import pandas as pd
import numpy as np
import os

# %%

chn_df = pd.read_csv('chinese_frequency_lists/words/hsk1-6.csv', 
                     delimiter='\t',
                     encoding= 'utf-8',
                     header= 'infer')

# %%

chn_df.head(n=5)

# %%

# %%

hex(ord(chn_df.iloc[0,2]))

# %%

chn_df.columns = ['hsk', 'hex', 'hanzi', 'pinyin', 'translation']

# %%
def hanzi_hex(hanzi : list):
    hanhex = []
    for han in hanzi:
        hanhex.append(hex(ord(han)))
    return hanhex

hanzi_hex_ser = chn_df.hanzi.apply(list).apply(hanzi_hex)

# %%

hanzi_hex_ser[0][0]

# %%

chr(int(hanzi_hex_ser[0][0], base=16))

# %%

chn_df.hex = hanzi_hex_ser

# %%

# chn_df.to_csv('hsk1-6_final.csv')

# %%

chn_anki_df = chn_df.filter(items=['pinyin', 'hanzi', 'hsk', 'translation'])

# %%

chn_anki_df
# %%
# chn_anki_df.to_csv('hsk1-6_anki_import.csv', encoding='utf-8', index=False)

# %%

path_to_vocab = "C:\\Users\\pat_h\\OneDrive\\p-spohr-repos\\Python-Resources\\projects\\ccta\\chinese_vocabulary_lists\\words\\raw"

# %%

mcf_df = pd.read_table(os.path.join(path_to_vocab, 'modern_character_freq.txt'), 
              encoding= 'gb2312', 
              delimiter='\t',
              skiprows= 5,
            #   nrows= 5,
              encoding_errors='replace',
              index_col= False,
              usecols= [1,2,3,4,5],
              header= 0,
              names = ['hanzi', 'freq', 'mutual', 'pinyin', 'eng'])
# %%

mcf_df.shape

# %%

print(chr(int('0xEF', base=16)))
print(chr(int('0xBF', base=16)))
print(chr(int('0xBD', base=16)))
print(chr(int('0xFFFD', base=16)))

# %%

replace_chr = print(chr(int('0xFFFD', base=16)))

# %%

mcf_df.loc[mcf_df['hanzi'] == replace_chr]

# %%

mcf_df.tail()

# %%

mcf_df[mcf_df.eng is np.nan]

# %%

mcf_df = mcf_df.loc[mcf_df.eng.notna()]

# %%

mcf_df = mcf_df.drop('mutual', axis=1)


# %%

mcf_df.hanzi.nunique()

# %%

mcf_df = mcf_df.reset_index()

# %%

mcf_df = mcf_df.drop(['level_0', 'index'], axis=1)

# %%

mcf_df.isna().apply(sum, 0)

# %%

mcf_df.to_csv('modern_characters_freq_cleaned.csv', sep='\t', index= False, encoding= 'utf-8')

# %%

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

