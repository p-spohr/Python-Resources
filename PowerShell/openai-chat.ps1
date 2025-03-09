# make sure to use approved verbs for cmdlet
# https://learn.microsoft.com/en-us/powershell/scripting/developer/cmdlet/approved-verbs-for-windows-powershell-commands?view=powershell-7.4
function Get-Answer {
    
    param (
        [ValidateSet('eng', 'deu')]
        [String] $Language = 'eng',
        [Parameter(Mandatory)]
        [String] $Prompt
    )
        
    $OPENAI_URL = 'https://api.openai.com/v1/chat/completions'
        
    $OPENAI_H = @{
        'Content-Type'  = 'application/json';
        'Authorization' = $('Bearer ' + $OPENAI_KEY)
    }

    if ($Language -eq 'eng') {
        
        $OPENAI_D = @{
            'model'    = 'gpt-4o';
            'messages' = 
            @{
                'role'    = 'user';
                'content' = $Prompt
            },
            @{
                'role'    = 'user';
                'content' = 'Explain in 3 sentences in English.'
            }
        }
        
        
    } else {
        
        $OPENAI_D = @{
            'model'    = 'gpt-4o';
            'messages' = 
            @{
                'role'    = 'user';
                'content' = $Prompt
            },
            @{
                'role'    = 'user';
                'content' = 'Erlären Sie in 3 Sätze in Deutsch.'
            }
        }

    }



    $myresponse = Invoke-WebRequest -Uri $OPENAI_URL -Headers $OPENAI_H -body (ConvertTo-Json $OPENAI_D) -Method Post

    $answer = ($myresponse.content | ConvertFrom-Json).choices[0].message.content

    Write-Output $answer
}
