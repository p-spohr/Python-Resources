
@echo off

Rem This exports registry hkcu 
echo "saving hkcu..."
reg query hkcu > reg.reg
echo "success"

Rem Print results of new file
echo "printing..."
type reg.reg
echo "success"