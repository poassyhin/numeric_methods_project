import numpy as np
import math
from methods import dichotomy, newton_method, tangent_method, secant_method

EPS = 1e-6

def find_roots_in_range(M, f, a, b, EPS=1e-6):
        res = []
        root = M(f, a, b, EPS)
        if(root != None):
            return [root] + find_roots_in_range(M, f, a, root-2*EPS, EPS) + find_roots_in_range(M, f, root+2*EPS, b, EPS)
        else:
            return []


def filter_roots(roots, f, eps):
        new_roots = []
        roots.sort()
        for i in range(len(roots)-1):
                if(abs(roots[i]-roots[i+1]) <= 0.1):
                        roots[i] = ""
        for i in roots:
                if(i != ""):
                        new_roots.append(i)
        return new_roots

def solve(f, a, b, e):
  sol = {}
  sol.update({'dichotomy': filter_roots(find_roots_in_range(dichotomy,f, a, b, e), f, e)})
  sol.update({'newton_method': filter_roots(find_roots_in_range(newton_method,f, a, b, e), f, e)})
  sol.update({'tangent_method': filter_roots(find_roots_in_range(tangent_method,f, a, b, e), f, e)})
  sor_sol = {len(sol[i]): i for i in sol.keys()}
  r_key = sorted(sor_sol, reverse=True)[0]
  return sor_sol[r_key], sol[sor_sol[r_key]]

def f(x):
    return -2*x**10+4*x**5+2*x**2-x

def main():
  print(filter_roots(find_roots_in_range(dichotomy, f, -10, 10, EPS), f, EPS))
  print(filter_roots(find_roots_in_range(newton_method, f, -10, 10, EPS), f, EPS))
  print(filter_roots(find_roots_in_range(tangent_method, f, -10, 10, EPS), f, EPS))
  print(secant_method(f, -10, 10, EPS))
  print(find_roots_in_range(dichotomy,f, -10, 10, EPS))
  met, ans = solve(f, -10, 11, EPS)
  print('Answer: {0}, Method: {1}'.format(ans, met)) 


if __name__ == "__main__":
  main()
