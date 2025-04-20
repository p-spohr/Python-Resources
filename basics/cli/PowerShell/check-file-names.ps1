$save_path = 'C:\Users\pat_h\OneDrive\public-repos\Python-Resources\gen_images'

function Test-Names {
    [CmdletBinding()]
    Param(
        [Parameter(Mandatory = $true)]
        [string] $Name
    )

    Process {

        Get-ChildItem $save_path | ForEach-Object -Process {if ($PSItem.Name -eq $Name + '.jpg') {Write-Output 'Name already exists.'}}

    }
}