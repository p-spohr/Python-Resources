function Send-Greeting {
    [CmdletBinding()]
    Param(
        [Parameter(Mandatory = $true)]
        [string] $Name
    )

    Process {
        Write-Host ("Hello " + $Name + "!")
    }
}

# in order to run this function/cmdlet

# import the file into PowerShell
# Import-Module <path-to-file>

# O use dot sourcing
# . <path-to-file>

# after it is in the current PowerShell enviroment, PS can recognized the name of the function

# use this to call function without importing file and pass the variables directly into the file
# if ($MyInvocation.MyCommand.CommandType -eq 'ExternalScript') {
#     $name = $args[0]
#     Send-Greeting $name
# }