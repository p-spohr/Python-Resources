# %%

import pandas as pd
import numpy as np
import os
import re

# %%

ccre = re.compile(r'(.+)\s(.+)\s\[(.+)\]\s/(.+)/')

res = ccre.search('11區 11区 [Shi2 yi1 Qu1] /(ACG) Japan (from the anime "Code Geass", in which Japan was renamed Area 11)/test/test/')

print(res.groups())

# %%

new_df = pd.DataFrame(columns=['traditional', 'simplified', 'pinyin', 'eng'])

# %%

with open(os.path.join('chinese_vocabulary_lists/raw', 'cc-cedict.u8'), encoding='utf-8', mode='r') as file:
    ccdict = file.read()
    
# %%

cclist = ccdict.split('\n')

# %%

ccprep = [line for line in cclist if line[0] != '#']

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

cc_df

# %%

hsk_df = pd.read_csv('chinese_vocabulary_lists/cleaned/hsk1-6_cleaned.csv', sep= '\t', encoding= 'utf-8')
hsk_df

# %%

inter_hsk_cc = np.intersect1d(cc_df.simplified, hsk_df.simplified)

# %%

inter_hsk_cc

# %%

diff_hsk_cc = np.setdiff1d(hsk_df.simplified, inter_hsk_cc)

# %%

diff_hsk_cc

# %%

hsk_df.loc[hsk_df.simplified.isin(diff_hsk_cc)].pinyin_char.to_numpy()

# %%

new_pinyin = ['da3 lan2 qiu2', 'xi4 ling3 dai4', 'niu3 kou4 er5', 'zhi4 li4 yu2']

# %%

add_to_ccdict = hsk_df.loc[hsk_df.simplified.isin(diff_hsk_cc)]

# %%

add_to_ccdict = add_to_ccdict.loc[:, ['traditional', 'simplified', 'pinyin_char', 'eng']]

# %%

add_to_ccdict.loc[:, 'pinyin_char'] = new_pinyin

# %%

add_to_ccdict = add_to_ccdict.rename(columns={'pinyin_char': 'pinyin'})

# %%

cc_df_1 = pd.concat([cc_df, add_to_ccdict], axis=0)

# %%

cc_df_1 = cc_df_1.reset_index(drop= True)

# %%

cc_df_2 = cc_df_1.loc[:, ['simplified', 'traditional', 'pinyin', 'eng']]

# %%

cc_df_2.to_csv('ccdict_cleaned.csv', sep= '\t', encoding= 'utf-8', index= False)

# %%

hsk_df_1 = hsk_df.merge(cc_df_2.loc[:, ['simplified', 'pinyin']], how= 'left', on= 'simplified')

# %%

hsk_df_1

# %%

(
    hsk_df_1
    .drop('pinyin_x', axis= 1)
    .rename(columns= {'pinyin_y': 'pinyin'})
    .loc[:, ['simplified', 'traditional', 'pinyin', 'eng', 'level']]
)

# %%

hsk_df_2 = (
                hsk_df_1
                .drop('pinyin_x', axis= 1)
                .rename(columns= {'pinyin_y': 'pinyin'})
                .loc[:, ['simplified', 'traditional', 'pinyin', 'eng', 'level']]
            )

# %%

for i in range(1, 7):
    
    file_name = f'hsk{i}_anki.csv'
    print(file_name)
    
    hsk_df_2.loc[hsk_df_2.level == i].to_csv(file_name, encoding= 'utf-8', index= False, sep= '\t')
    
    
# %%
