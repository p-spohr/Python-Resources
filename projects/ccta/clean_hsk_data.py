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

mcf_df = pd.read_csv('chinese_vocabulary_lists/cleaned/modern_characters_freq_cleaned.csv',
            encoding= 'utf-8',
            sep= '\t')

# %%

hsk_df = pd.read_csv('chinese_vocabulary_lists/cleaned/hsk1-6_cleaned.csv',
            encoding= 'utf-8',
            sep= '\t')

# %%

# missing_char = pd.Series(['啰', '囉', 'luo1', 'phonetic', pd.NA], index= mcf_df.columns)

# mcf_df = pd.concat([mcf_df, missing_char.to_frame().T], axis=0, ignore_index= True)

# %%

# mcf_df.to_csv('modern_characters_freq_cleaned.csv', 
#               sep='\t', 
#               index= False, 
#               encoding= 'utf-8')

# %%

hsk_df

# %%

def character_converter(ser_data : pd.Series, ref_df : pd.DataFrame, simplified : bool = True):
    '''
    word: characters
    ref_df: dataframe with simplified and traditional characters
    simplified: convert simplified characters to traditional characters
    '''
    char_list = list(ser_data)
    original_char_list = []
    converted_char_list = []
    pinyin_list = []
    error_check = False
    
    if simplified:
        from_type = 'simplified'
        to_type = 'traditional'
    else:
        from_type = 'traditional'
        to_type = 'simplified'
        
    
    for char in char_list:
        
        found_char = ref_df.loc[ref_df[from_type] == char]
        
        if found_char.size > 0:
            original_char_list.append(found_char.loc[:, [from_type]].to_numpy().flatten()[0])
            converted_char_list.append(found_char.loc[:, [to_type]].to_numpy().flatten()[0])
            pinyin_list.append(found_char.loc[:,['pinyin']].to_numpy().flatten()[0])
            
        
        else:
            converted_char_list.append('#')
            error_check = True

    return pd.Series(
        {
        'simplified' : ''.join(original_char_list),
        'traditional': ''.join(converted_char_list), 
        'pinyin_new': ' '.join(pinyin_list),
        'error': error_check
        }
        )
    

# %%

character_converter(hsk_df.loc[16, 'word'], mcf_df)

# %%

converted_characters_df = hsk_df.word.apply(character_converter, args= (mcf_df, True))

# %%

converted_characters_df[converted_characters_df.error == True]

# %%

converted_characters_df

# %%

hsk_df

# %%

hsk_df = hsk_df.merge(converted_characters_df, left_on= 'word', right_on = 'simplified')

# %%

hsk_df.isna().sum(0)

# %%

hsk_df = hsk_df.rename(columns={'pinyin_new': 'pinyin_char'})

# %%

hsk_df = hsk_df.loc[:, ['level', 'simplified', 'traditional', 'pinyin', 'eng', 'pinyin_char']]

# %%

# hsk_df.to_csv('hsk1-6_cleaned.csv', encoding='utf-8', index= False, sep= '\t')

# %%
