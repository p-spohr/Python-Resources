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
