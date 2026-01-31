# play_sound

# %%

import pygame
import random

lazer_path = 'C:\\Users\\pat_h\\OneDrive\\Desktop\\Kenney Game Assets All-in-1 2.0.0\\Audio\\Sci-Fi Sounds\\Audio\\laserSmall_002.ogg'

# %%
rand_freq = random.randint(30000,60000)
rand_vol = random.randint(10,30) / 100

print(f'Frequency: {rand_freq}')
print(f'Volume: {rand_vol}')

# %%
# pygame.init()
pygame.mixer.init(frequency=rand_freq, size=-16, channels=2, buffer=512)
lazer = pygame.mixer.Sound(lazer_path)

# %%

secs = lazer.get_length()

#%%

secs * 5    

# %%

waiting = int(round(secs, 1) * 1000)


# %%

lazer.set_volume(rand_vol)
lazer.play()
pygame.time.wait(waiting)
# time.sleep(secs)