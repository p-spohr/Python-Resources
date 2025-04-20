# %%
import os
    
# %%
path_lists = '../chinese_frequency_lists/characters'
# os.path.exists(os.path.join(path_lists, 'modern.txt'))
complete_path = os.path.join(path_lists, 'modern.txt')
# %%
with open(complete_path, mode='r', encoding='utf-8', errors='replace') as txt_file:
    raw_text = txt_file.read()
# %%
for line in raw_text.split('\n')[0:10]:
    print(line)
# %%
import codecs


# %%
codecs.lookup('gb2312')
# %%

path_fiction = os.path.join(path_lists, 'fiction.txt')

# %%
with open(path_fiction, mode='r', encoding='gb2312', errors='replace') as txt_file:
    raw_text_fiction = txt_file.read()
# %%

for line in raw_text_fiction.split('\n')[0:10]:
    print(line)

# %%

def detect_encoding(file_path : str):
    if not os.path.exists(file_path):
        raise FileNotFoundError('Please use correct file name.')
    else:
        encodings = all_encodings_python
        actual_encoding = ''
        for enc in encodings:
            try:
                with open(file_path, encoding=enc, errors='strict') as file:
                    file.read()
                actual_encoding = enc
            except UnicodeError:
                continue
        if actual_encoding != '':
            print(f'The encoding is {actual_encoding}.')
        else:
            print('Current encoding not in list.')        

# %%

detect_encoding('C:\\Users\\pat_h\\OneDrive\\p-spohr-repos\\Python-Resources\\chinese_frequency_lists\\characters\\fiction.txt')

# %%

detect_encoding('C:\\Users\\pat_h\\OneDrive\\p-spohr-repos\\Python-Resources\\chinese_frequency_lists\\characters\\modern.txt')
# %%

os.path.exists('C:\\Users\\pat_h\\OneDrive\\p-spohr-repos\\Python-Resources\\chinese_frequency_lists\\characters\\modern.txt')
# %%

import codecs

# %%
codecs.Codec.__dict__

# %%

with open('all_encodings.txt', mode='r') as file:
    all_encodings_python = file.read()

# %%
all_encodings_python = all_encodings_python.split('\n')
# %%
all_encodings_python.remove('')
# %%
all_encodings_python
# %%
