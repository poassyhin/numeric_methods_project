import numpy as np
import math
import time
import random
from utils import derivative

def __init__():
    warnings.filterwarnings("ignore")

def dichotomy (fun, a,b, EPS):
    n = 1000
    res = []
    setka=np.linspace(a, b, n)
    
    for x,y in zip(setka, setka[1:]):
        if fun(x) * fun(y) > 0:
            continue
        root = None
        while ( abs(fun(y)-fun(x)) )>EPS:   
            mid = (y+x)/2              
            if fun(mid) == 0 or abs(fun(mid))<EPS:  
                root = mid
                break
            elif (fun(mid) * fun(x)) < 0:   
                y = mid            
            else:
                x = mid
        if(root == None):
            mid = (y+x)/2              
            if fun(mid) == 0 or fun(mid)<EPS:  
                root = mid

            elif (fun(mid) * fun(x)) < 0:   
                y = mid            
            else:
                x = mid
        if(root != None):
            return root

def newton_method(f, a, b, EPS=1e-6, METHOD_TIMEOUT=5):
    start_time = time.time()
    seeking_range = b - a

    for i in range(20):                           # Making (almost) sure it is close enough
        x = a + random.random() * seeking_range   # to come down to the right value
        #print(x)
        try:
            time_consumed = time.time() - start_time
            while (abs(f(x)) > EPS) and (time_consumed < METHOD_TIMEOUT):
                x = float(x - f(x) / derivative(f, x, dx=EPS))

                if (x < a) or (b < x): # Checking if x is within the range (a; b)
                    break

                if (abs(f(x)) <= EPS):# Correct solution
                    #print(EPS)
                    return x
                time_consumed = time.time() - start_time
        except Exception as e:
            pass

    return None

def secant_method(f,a,b,e):
    condition = True
    c = a - (b - a) * f(a) / (f(b) - f(a))
    while condition:
        if f(a) == f(b):
            break
        c = a - (b - a) * f(a) / (f(b) - f(a))
        a = b
        b = c
        condition =(abs(f(c)) > e)

    return [c]


def simple_itter_method(fun, a, b, e=1e-6):
    x1 = (a + b) / 2

    x0 = x1
    x1 = fun(x0)
    while((x1>b) | (x1<a)):
        if ((x1 > b) | (x1 < a)):
            x1 = (x1 + (a + b) / 2) / 2
        while abs(x1 - x0) <= e:
            x0 = x1
            x1 = fun(x0)
    return x1


def tangent_method(f, a, b, EPS=1e-6, METHOD_TIMEOUT=5):
    start_time = time.time()
    seeking_range = b - a

    for i in range(20):                           # Making (almost) sure it is close enough
        x = a + random.random() * seeking_range   # to come down to the right value
        derivative_value = derivative(f, x, dx=EPS)
        try:
            time_consumed = time.time() - start_time
            while (abs(f(x)) > EPS) and (time_consumed < METHOD_TIMEOUT):
                x = float(x - f(x) / derivative_value)

                if (x < a) or (b < x): # Checking if x is within the range (a; b)
                    break

                if (abs(f(x)) <= EPS): # Correct solution
                    return x
                time_consumed = time.time() - start_time
        except Exception as e:
            pass

    return None
