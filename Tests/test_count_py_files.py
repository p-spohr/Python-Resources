# test walk path time
# %%
import time
import os


# %%

start_time = time.time()
print('Starting py count...')

# %%

onedrive_path = 'C:\\Users\\pat_h\\OneDrive'
count = 0
for root, direct, files in os.walk(onedrive_path):
    for file in files:
        if file[-3:] == '.py':
            count += 1
            # print(os.path.basename(file))


# %%

end_time = time.time()
print(f'There are {count} py files.')
print(f'Time: {round(end_time - start_time, 3)}')