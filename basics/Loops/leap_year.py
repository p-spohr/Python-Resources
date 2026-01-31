# %%
years = [1020, 1500, 1800, 2000, 2004, 2024, 3000, 3054]

for year in years:

    if year % 4 == 0: 

        leap_year = True

        if year % 100 == 0 and not year % 400  == 0: 

            leap_year = False 

    else: 

        leap_year = False 
            
    if leap_year: 

        print(year, "is a leap year!") 
            
    else: 

        print(year, "isn't a leap year!")

# %%

