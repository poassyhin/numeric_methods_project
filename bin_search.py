import numpy as np


def dichotomy (fun, a,b, eps):
    n = 1000
    res = []
    setka=np.linspace(a, b, n)
    
    for x,y in zip(setka, setka[1:]):
        if fun(x) * fun(y) > 0:
            continue
        root = None
        while ( abs(fun(y)-fun(x)) )>eps:   
            mid = (y+x)/2              
            if fun(mid) == 0 or abs(fun(mid))<eps:  
                root = mid
                break
            elif (fun(mid) * fun(x)) < 0:   
                y = mid            
            else:
                x = mid
        if(root == None):
            mid = (y+x)/2              
            if fun(mid) == 0 or fun(mid)<eps:  
                root = mid

            elif (fun(mid) * fun(x)) < 0:   
                y = mid            
            else:
                x = mid
        if(root != None):
            return root



