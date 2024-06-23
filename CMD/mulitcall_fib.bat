@ECHO OFF
@REM call the fibonacci code in the same terminal

SET setWD=C:\Users\pat_h\OneDrive\public-repos\Python-Resources
SET pyFile=C:\Users\pat_h\OneDrive\public-repos\Python-Resources\fibseq.py
SET pyResults=C:\Users\pat_h\OneDrive\public-repos\Python-Resources\results

@REM when using >> it locks the file and the second terminal cannot accesses it when it starts
@REM so a second file needs to be created

@REM START "PY 1" /d %setWD% CMD /c "PY %pyFile% >> fibresults1.txt"

@REM START "PY 2" /d %setWD% CMD /c "PY %pyFile% >> fibresults2.txt"

IF not exist %pyResults% (
    MKDIR %pyResults%
)

FOR /l %%N IN (1, 1, 10) DO (
    ECHO %%N process has begun..
    START "PY %%N" /d %setWD% CMD /c "PY %pyFile% >> %pyResults%\fibresults%%N.txt"
)