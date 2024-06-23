@REM set varaible
@ECHO OFF

@REM can set commands as variables, but %E% and %S% are not much shorter or quicker to write
SET E=ECHO
SET S=SET
SET T=variable_to_batch.txt


@REM SET /p opens input prompt, but we can skip it by using =< to automatically set the variable
CALL CMD /c ^
 "%E% first call.. && %S% /p fromText=<%T% && %S% fromText"

@REM in this case I don't need to set the variable inside of a CALL CMD, so I can do it directly in the bat
SET /p fromText=<%T%

@REM the set variable fromText is not stored from the first call, so it can't be passed to another command
@REM the variable needs to be set directly in the bat file to be stored in the caller terminal
CALL CMD /c ^
 "ECHO second call .. && ECHO the variable from the file %T% is %fromText%"
