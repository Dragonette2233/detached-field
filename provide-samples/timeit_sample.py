import re
from timeit import timeit
import sys

class TrassPasser():
    pass

def decor(func):
    def inner(*args, **kwargs):
        if args:
            print(f'Decor vars: args - {args}')
        elif kwargs:
            print(f'Decor vars: kwargs - {kwargs}')
        else:
            print(f'Decor vars: args - {args}, kwargs - {kwargs}')
        func(*args, **kwargs)
        
    return inner

def makelist_1():
    result = []
    for val in range(1000):
        result.append(val)
    return result

def makelist_2():
    return [val for val in range(1000)]

print(f"First way: {timeit(makelist_1, number=1000)} seconds")
print(f"Second way: {timeit(makelist_2, number=1000)} seconds")
    


            
            