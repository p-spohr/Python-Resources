# Accessing Git with Python

# %%

import subprocess

# %%

subprocess.Popen(args= ['C:/Users/pat_h/Git/git-cmd.exe', 'dir'])

# %%

git_process = subprocess.Popen(args= ['C:/Users/pat_h/Git/git-cmd.exe', '/c', 'dir'], text= True)

print(git_process.stdout)

# %%

subprocess.run(args= ['C:/Users/pat_h/Git/git-cmd.exe', '/c', 'dir'])
 

# %%


# %%

subprocess.Popen(['C:\WINDOWS\system32\cmd.exe', '/c', 'start Obsidian.exe'], cwd= 'C:/Users/pat_h/AppData/Local/Obsidian')


# %%

cmd_process = subprocess.run(['C:\WINDOWS\system32\cmd.exe', '/c', 'dir'], text= True, capture_output= True)
print(cmd_process.stdout)
print(cmd_process)

# %%

import subprocess

# %%

## WORKS!
dir_process = subprocess.Popen(['C:\\WINDOWS\\system32\\cmd.exe', '/c', 'dir'], text= True, stdout= subprocess.PIPE)
print(dir_process)
print(dir_process.stdout)
print(dir_process.communicate()[0])

# %%

## WORKS!
git_process = subprocess.Popen(['C:\\WINDOWS\\system32\\cmd.exe', '/c', 'git status'], text= True, stdout= subprocess.PIPE)
print(git_process)
print(git_process.stdout)
print(git_process.communicate()[0]) # communicate returns tuple with stdout and stderr

# %%

## WORKS!
git_process = subprocess.Popen(['C:\\WINDOWS\\system32\\cmd.exe', '/c', 'git diff Navigation.py'], text= True, stdout= subprocess.PIPE)
print(git_process)
print(git_process.stdout)
print(git_process.communicate()[0]) # communicate returns tuple with stdout and stderr