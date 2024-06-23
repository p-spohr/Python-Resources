@ECHO OFF
@REM use at the command line
@REM for /r %i in (*) do @(type %~fi)
@REM do @() with @ will not echo the command

@REM use in batch file
FOR /r %%F IN (*.txt) DO @(
    ECHO -----%%~nF-----
    TYPE %%~fF
    )

@REM %%F with two % is needed to run in the batch file
@REM /r is for files in CD 
@REM (*) is for all files in CD, (*.txt) is for all files with txt extensions
@REM ~f returns full file path when placed between %F
@REM ~n returns the file name when placed between %F