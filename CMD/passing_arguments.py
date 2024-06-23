# passing arguments into Python script

# %%

import sys
import os
import io
import re

# %%

print("---Getting Arguments from---")
print(f"DIR: {os.getcwd()}")
print(f"FILE: {os.path.split(__file__)[1]}")
print(f"ARG 1: {sys.argv[1]}")
print(f"{sys.argv[0]} = {os.path.split(__file__)[1]}") # 0 argument is file name

# CMD
# $[pat] C:\Users\pat_h\OneDrive\public-repos\Python-Resources > py passing_arguments.py "SUCCESS!"

# STDOUT
# ---Getting Arguments from---
# DIR: C:\Users\pat_h\OneDrive\public-repos\Python-Resources
# FILE: passing_arguments.py
# ARG 1: SUCCESS!
# passing_arguments.py = passing_arguments.py

# %%

with open("passing_arguments_output.txt", "r", encoding= "utf-8") as pa_output:
    print(pa_output.read())
    print(type(pa_output.read()))



# %%

with open("passing_arguments_output.html", "r", encoding= "utf-8") as pa_output:
    print(pa_output.read())
    print(type(pa_output.read()))


# %%

simple_text = "HI!(newline)\nThis text has special(tab)\tcharacters."
print(simple_text)
print(repr(simple_text))


# %%

with open("passing_arguments_output.txt", "r", encoding= "utf-8") as pa_output:
    get_args = pa_output.read()

# %%

get_args

re.compile("DIR: {}")
