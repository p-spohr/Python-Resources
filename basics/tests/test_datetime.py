# test_datetime.py
# %%
import datetime
import time
# %%

my_date = datetime.date(day=1, month=2, year=1994)

next_days = datetime.date(day=5, month=2, year=1994)

# %%

my_date - next_days

# %%

time.time()

# %%

x = datetime.datetime.today() - datetime.timedelta(seconds=time.time())


# %%

x.isoformat()

# %%

x.strftime('%A, %d.%m.%y')

# %%

datetime.timedelta.days

# %%

datetime.datetime.today()

# %%
datetime.date.today()
# %%
