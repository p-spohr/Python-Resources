
# öffnet File Explorer (Windows)
New-Alias -Name exp -Value explorer.exe


# initialisiere neue Aliases für schnelle Repo Navigation 
New-Alias -Name rrr -Value Set-R-Repo -Description "Set current path to p-spohr R-Resource repo"

New-Alias -Name prr -Value Set-Python-Repo -Description "Set current path to p-spohr Python-Resource repo"

New-Alias -Name hbp -Value Set-Pytorium-Repo -Description "Set current path to p-spohr HTW-Berlin-Pytorium repo"


# mache Repo Path als Workingpfad 
function Set-R-Repo ($folder = "a") {

  Set-Location C:\Users\pat_h\OneDrive\public-repos\R-Resources
  
  # zusätzlicher Parameter, wobei man File Explorer öffnet
  if ($folder -eq "f") {
    exp .\
  }

}

function Set-Python-Repo ($folder = "a") {

  Set-Location C:\Users\pat_h\OneDrive\public-repos\Python-Resources
  if ($folder -eq "f") {
    exp .\
  }
}

function Set-Pytorium-Repo ($folder = "a") {

  Set-Location C:\Users\pat_h\OneDrive\public-repos\HTW-Berlin-Pytorium
  if ($folder -eq "f") {
    exp .\
  }
}

