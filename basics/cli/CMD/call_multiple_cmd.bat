@REM call multiple cmd
@ECHO OFF

SET repoPath=C:\Users\pat_h\OneDrive\public-repos\Python-Resources
SET returnPath=C:\Users\pat_h

@REM the best I can do to split up the long command in shorter lines is to use /k ^ since the string command needs to be in one line
@REM make sure to put a space on the next line after ^ since the next character on the new line is escaped
START "Set Variable Test" CMD /k ^
 "ECHO HI from Set Variable Test && ECHO AND THERE"

@ REM the only way to make it short on the command line string is to set variables
START "Multiple prompts on one line test" CMD /k ^
 "CD %repoPath%  && PY fibseq.py && SET fromText=testvar && SET fromText && ECHO ..end && CD %returnpath%"

@REM call the cmd to have the commands run in the same terminal
@REM make sure to put a space on the next line after ^ since the next character on the new line is escaped
@REM when calling multiple CALL then use /c to close the terminal since /k will keep it open and stop the next CALL from running
CALL CMD /c ^
 "ECHO HI from Set Variable Test && ECHO AND THERE"


@ REM the only way to make it short on the command line string is to set variables
CALL CMD /c ^
 "CD %repoPath%  && PY fibseq.py && SET fromText=testvar && SET fromText && ECHO ..end && CD %returnpath%"
