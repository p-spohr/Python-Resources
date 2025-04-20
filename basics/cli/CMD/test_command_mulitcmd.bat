
@echo off

Rem This starts multiple cmd terminals, prints a message, and then runs python script

start "TF" /d C:\Users\pat_h\anaconda\envs\tf cmd /k "echo 'first TF' && echo 'HI' && dir && py C:\Users\pat_h\OneDrive\public-repos\Python-Resources\fibseq.py && py C:\Users\pat_h\OneDrive\public-repos\Python-Resources\fibseq.py"

start "HTW" /d C:\Users\pat_h\anaconda\envs\htwberlin cmd /k "echo 'first HTW' && echo 'HI' && dir && py C:\Users\pat_h\OneDrive\public-repos\Python-Resources\fibseq.py && py C:\Users\pat_h\OneDrive\public-repos\Python-Resources\fibseq.py"

start "TF2" /d C:\Users\pat_h\anaconda\envs\tf cmd /k "echo 'second TF' && echo 'HOWDY' && dir && py C:\Users\pat_h\OneDrive\public-repos\Python-Resources\fibseq.py && py C:\Users\pat_h\OneDrive\public-repos\Python-Resources\fibseq.py"

start "HTW2" /d C:\Users\pat_h\anaconda\envs\htwberlin cmd /k "echo 'second HTW' && echo 'HOWDY' && dir && py C:\Users\pat_h\OneDrive\public-repos\Python-Resources\fibseq.py && py C:\Users\pat_h\OneDrive\public-repos\Python-Resources\fibseq.py"

Rem use the python.exe directly in the folder
start "TF3" /d C:\Users\pat_h\anaconda\envs\tf cmd /k "echo 'directly TF' && echo 'SUP' && dir && C:\Users\pat_h\anaconda\envs\tf\python.exe C:\Users\pat_h\OneDrive\public-repos\Python-Resources\fibseq.py && C:\Users\pat_h\anaconda\envs\tf\python.exe C:\Users\pat_h\OneDrive\public-repos\Python-Resources\fibseq.py"

Rem IMPORTANT
Rem Need to check if it is working correctly by saving results to a file
Rem Check to see if using python.exe in different environments actually speeds up process
Rem It looks like py command uses the default python.exe in Apps, but I need to use specific environments when I use different libraries
Rem Test if the environments are working properly by testing specific libraries