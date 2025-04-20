# %%

characters = "你好世界"
for char in characters:
    print(f"{char}: {ord(char):X}") # prints code
    
# %%

characters = "你好世界"
for char in characters:
    print(f"{char}: {ord(char)}") # prints number
    
# %%

char = '你'
print(f"Character: {char}")
print(f"Decimal: {ord(char)}")
print(f"Hexadecimal: {ord(char):X}")
print(f"Binary: {bin(ord(char))[2:]}")
print(f"Octal: {oct(ord(char))[2:]}")


# %%

with open('chinese_test_ledger.csv', encoding='UTF-8') as chn_test:
    ledger = chn_test.read()
# %%

print(ledger.split('\n'))

# %%

import re
# %%

m = re.match(r'<tr>(.*)</tr>', '<tr>hi</tr>')
print(m.group(1))
print(m.groups())
# %%
html_path = 'C:\\Users\\pat_h\\OneDrive\\p-spohr-repos\\Python-Resources\\CCTA\\encoding_raw.html'
with open(html_path) as html_file:
    raw_html = html_file.read()
# %%
all_encodings = []
for line in raw_html.split('\n'):
    # print(line)
    try:
        m = re.search(r'<tr class="row-\w*"><td><p>(.*)</p></td>', line)
        print(m.groups())
        all_encodings.append(m.group(1))
    except AttributeError:
        continue
# %%
all_encodings

# %%

with open('all_encodings.txt', mode='w') as file:
    for item in all_encodings:
        file.write(f'{str(item)}\n')

# %%
