# multiple fib seq running

# %%

import time
import sys

# %%

start_time = time.time()

# correct!
def fib_seq(n=1):

    a, b = 0, 1

    for i in range(0, n):

        a, b = b, a + b
        # this sets the variables at the same time which will use a previous value not a = b

    return a

# %%

# check to see if more than 1 argument is passed
if len(sys.argv) < 2:
    
    print("Please input number greater than 1")

else:

    n_value = int(sys.argv[1])
    fib_value = fib_seq(n_value)

    end_time = time.time()

    print(f'n:= {n_value}')
    print(f'f(n)= {fib_value}')
    print(f'Time Elapsed: {round(end_time - start_time, 6)}')


# %%

# start_time = time.time()

# for i in range(1,11):
#     print(i)
#     fib_seq(1000000)

# end_time = time.time()

# print(f'Time Elapsed: {round(end_time - start_time, 2)}')
# %%

# # %%

# # incorrect value
# def f(n):

#     a = 0
#     b = 1

#     for i in range(0, n):

#         print(f'a: {a}')
#         print(f'b: {b}')
        
#         a = b
#         b = a + b
#         # this sets the variables one after the other which uses a = b in the next expression b = a + b

#         print(f'=a: {a}')

#     return a

# f(3)
