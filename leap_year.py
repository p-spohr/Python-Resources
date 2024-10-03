# %%
jahr = int(input("Jahreszahl: ")) 

if jahr % 4 == 0: 

    if jahr % 100 == 0: 

        if jahr % 400 == 0: 

            schaltjahr = True 

        else: 

            schaltjahr = False 
    
    else: 

        schaltjahr = True 

else: 

    schaltjahr = False 
        
if schaltjahr: 

    print(jahr, "ist ein Schaltjahr") 
        
else: 

    print(jahr, "ist kein Schaltjahr")

# %%

