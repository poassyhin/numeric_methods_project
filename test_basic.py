import bin_search
def solve(f, a, b, e):
  print(bin_search.dichotomy(f, a, b, e))

def main():
  solve(lambda x: x**3-x+1, -10, 10, 0.0001)

if __name__ == "__main__":
  main()
