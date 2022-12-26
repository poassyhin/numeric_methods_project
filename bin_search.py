import numpy as np

def f(fun, x):
    return eval(fun)

def dichotomy (fun, a,b, eps):
    n = 1000
    res = []
    setka=np.linspace(a, b, n)

    for x,y in zip(setka, setka[1:]):
        if f(fun,x) * f(fun,y) > 0:
            continue
        root = None
        while ( abs(f(fun,y)-f(fun,x)) )>eps:   
            mid = (y+x)/2              
            if f(fun,mid) == 0 or f(fun,mid)<eps:  
                root = mid                
                break
            elif (f(fun,mid) * f(fun,x)) < 0:   
                y = mid            
            else:
                x = mid          
        if root != None:
            res.append(root)
    return res
