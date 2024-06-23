# pass arguments from batch but with lists

import sys

# print script name that recieves arguments
print(f'Script: {sys.argv[0]}')

# print the first list "1 2 3"
print('First list:')
for num in sys.argv[1]:
    print(num)

# print the second list "4 5 6"
print('Second list:')    
for num in sys.argv[2]:
    print(num)