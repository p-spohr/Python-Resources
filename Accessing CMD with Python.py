# Accessing Python Shell

# %%

import subprocess


# %%

## list current working directory
result = subprocess.run(["dir"], shell=True, capture_output=True, text=True)
# capture output saves text to stdout
# text returns the text in character format not bytes

print(subprocess.run('dir', shell= True))
print(result.stdout)

# %%


# %%
## get directory of parent
result = subprocess.run(['cmd', '/c', 'cd ..', '&&', 'dir'], capture_output=True, text=True)
# cmd starts Command Prompt 
# /c readys prompt to accept string of characters
# cd .. goes to parent
# && connects commands
# dir lists directory

print(result.stdout)
print(result.stderr)

# %%

obsid_path = 'C:/Users/pat_h/AppData/Local/Obsidian'

subprocess.run(['cmd', '/c', '/s', f'cd "{obsid_path}"', '&&', 'dir'], capture_output=True)

# %%
## get directory of parent
result = subprocess.run(['cmd', '/c', f'cd {obsid_path}', '&&', 'dir'], capture_output=True, text=True)
# cmd starts Command Prompt 
# /c readys prompt to accept string of characters
# cd <path> goes to path
# && connects commands
# dir lists directory

print(result.args)
print(result.stdout)
print(result.stderr)


# %%

result = subprocess.run("cmd /c cd C:/Users/pat_h/AppData/Local/Obsidian && dir *.exe", capture_output= True, text= True)
# cmd starts Command Prompt 
# /c readys prompt to accept string of characters
# cd <path> changes directory
# && connects commands
# dir *.exe lists all files that end with .exe (* is a wildcard character that tries all characters in place of the *)

print(result.args)
print(result.stdout)
print(result.stderr)

# subprocess.run(['cmd', '/c', f'cd {obsid_path}', '&&', 'dir *.exe'], capture_output=True, text=True)
# doesn't work for some reason

# %%

result = subprocess.run(['cmd', '/c', 'cd C:/Users/pat_h/AppData/Local/Obsidian && start Obsidian.exe'], capture_output= True, text= True)
# cmd starts Command Prompt 
# /c readys prompt to accept string of characters
# cd <path> changes directory
# && connects commands
# dir *.exe lists all files that end with .exe (* is a wildcard character that tries all characters in place of the *)

print(result.args)
print(result.stdout)
print(result.stderr)

# subprocess.run(['cmd', '/c', f'cd {obsid_path}', '&&', 'dir *.exe'], capture_output=True, text=True)
# doesn't work for some reason
