#!
# %%

import time


# %%
print('Starting sleep...')
start_time = time.time()

time.sleep(3)

end_time = time.time()

print(f'Run Time: {round(end_time - start_time, 3)}')


# %%

num = 1

match num:
    case 1:
        print('one')
    case 2:
        print('two')
    case _:
        print('not one or two')
