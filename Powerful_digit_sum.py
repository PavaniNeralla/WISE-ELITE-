from itertools import count
def permuted_multiples():
  for x in count(start=1000):
    digits = sorted(str(2 * x))
    if all(sorted(str(x * k)) == digits for k in range(6, 2, -1)):
      return x
permuted_multiples()
