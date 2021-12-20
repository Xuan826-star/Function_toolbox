import numpy as np

def factorial(num:int):
    if num < 0:
        raise RuntimeError('negative input') 
    elif num == 0:
        return 1
    else:
        res=1
        for i in range(1,num+1):
            res*=i
        return res

