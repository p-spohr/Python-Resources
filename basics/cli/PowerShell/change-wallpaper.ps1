# $wallpaper_path = 'C:\Users\pat_h\AppData\Local\Microsoft\Windows\Themes\RoamedThemeFiles\DesktopBackground'
$save_path = 'C:\Users\pat_h\OneDrive\public-repos\Python-Resources\gen_images'

function Get-Image {
    
    param (
        # Must be one of 1024x1024, 1792x1024, or 1024x1792 for dall-e-3 models.
        [Parameter(Mandatory)]
        [ValidateSet('1024x1024', '1792x1024', '1024x1792')]
        [String] $Size,
        [Parameter(Mandatory)]
        [String] $Prompt,
        [Parameter(Mandatory)]
        [String] $Name,
        [Switch] $Wallpaper
    )
    
    Get-ChildItem $save_path | ForEach-Object -Process {if ($PSItem.Name -eq $Name + '.jpg') {$file_exists = $true}}

    if ($file_exists) {
        Write-Error -Message 'File name already exists. Please try again with new name.' -Category InvalidArgument -ErrorAction Stop
    }

    $OPENAI_URL = 'https://api.openai.com/v1/images/generations'
        
    $OPENAI_H = @{

        'Content-Type'  = 'application/json';
        'Authorization' = $('Bearer ' + $OPENAI_KEY)

    }


    $OPENAI_D = @{

        'model'  = 'dall-e-3';
        'prompt' = $Prompt;
        'n'      = 1;
        'size'   = $Size
        
    }
    
    Write-Output 'Generating image...'
    
    try {
        
        $response = Invoke-WebRequest -Uri $OPENAI_URL -Headers $OPENAI_H -body (ConvertTo-Json $OPENAI_D) -Method Post
        Write-Host 'OpenAI request successful!' -ForegroundColor Green
    }
    
    catch {
        
        Write-Error -Message 'Could not generate image.' -ErrorAction Stop
        
    }
    
    Write-Output 'Downloading image...'

    try {
        
        $picture_url = ($response.content | ConvertFrom-Json).data.url
        
        $full_name = $($Name + '.jpg')
        $new_save_path = $(Join-Path -Path $save_path -ChildPath $full_name)

        Invoke-WebRequest -Uri $picture_url -Method Get -OutFile $new_save_path

        Write-Host $($Name + ' saved successfully!') -ForegroundColor Green
    
    }
    
    catch {
        
        Write-Error -Message 'Could not download and save image.' -ErrorAction Stop
        
    }
    
    if ($Wallpaper) {

        Set-ItemProperty -Path 'HKCU:\Control Panel\Desktop' -Name Wallpaper -Value $new_save_path
        
        C:\Windows\System32\rundll32.exe user32.dll, UpdatePerUserSystemParameters 1, False
        C:\Windows\System32\rundll32.exe user32.dll, UpdatePerUserSystemParameters 1, True
        C:\Windows\System32\rundll32.exe user32.dll, UpdatePerUserSystemParameters 1, False

        for ($i = 0; $i -lt 5; $i++) {

            # no idea why this works to refresh the wallpaper
            # https://superuser.com/questions/398605/how-to-force-windows-desktop-background-to-update-or-refresh
            # https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/rundll32
            # https://support.microsoft.com/en-us/topic/how-to-correct-common-user32-dll-file-errors-3b34cc67-5741-ce2b-cc7d-86d5410f44f4
            # The full file path needs to be included for rundll32.exe or it will not work in the script
            # this must be run several times since it doesn't always work 🤷
            C:\Windows\System32\rundll32.exe user32.dll, UpdatePerUserSystemParameters 1, True
        
        }
        
        Write-Host 'Image set as wallpaper! Log out and log back in if changes do not show automatically.' -ForegroundColor Green

    }
    
}