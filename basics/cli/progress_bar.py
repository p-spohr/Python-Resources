import time
import random


def progress_bar(progress, total):
    bar_length = 75
    percent = progress / total
    bar = '#' * int(bar_length * percent) + '-' * int(bar_length * (1-percent))
    print(f'\r|{bar}| {100*percent:.2f}%', end='', flush=True)

length = 50
load_progress = []
load_size = 0
for i in range(length):
    load_size += random.randint(1, 12)
    load_progress.append(load_size)

for prog in load_progress:
    time.sleep(0.12)
    progress_bar(prog, load_size)

print()  # final newline


# def progress_bar(progress, total):
#     percent = progress / total
#     bar_len = 50
#     filled = int(bar_len * percent)
#     bar = '#' * filled + '-' * (bar_len - filled)
#     print(f'\r|{bar}| {percent*100:.2f}%', end='', flush=True)

# # simulate uneven loading
# load_progress = []
# load_size = 0
# for _ in range(50):
#     load_size += random.randint(1, 8)
#     load_progress.append(load_size)

# for prog in load_progress:
#     time.sleep(0.12)
#     progress_bar(prog, load_size)

# print()