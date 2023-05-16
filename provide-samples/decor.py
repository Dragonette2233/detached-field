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


    


            
            