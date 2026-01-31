# edit_google_search

# %%

combined = ""

with open("google_search_output.txt","r") as output:
    
    edit = output.read().split("\n")
    edit = edit[0:-1] # returns all but last postion (which is '')
    len_list = len(edit) # imporant for adding + at end
    
    for word in edit:
        
        word = word.strip() # get rid of whitespace
        len_list -= 1 # when len == 0 then add word without +
        
        if len_list > 0:
            combined += f'{word}+'
        else:
            combined += f'{word}' # don't add + to last word

with open("google_search_output.txt","w") as output:
    output.write(combined)

