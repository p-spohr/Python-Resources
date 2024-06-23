$FirstName = Read-Host -Prompt "First Name"
$LastName = Read-Host -Prompt "Last Name"

$Year = (Get-Date).Year 
$Month = (Get-Date).Month
$Day = (Get-Date).Day

New-Item -Value "$FirstName $LastName" -ItemType File -Path ".\$Year-$Month-$Day $FirstName $LastName.txt"
