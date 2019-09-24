import sympy
def All_4digitNumbers():
  return [i for i in range(1000,9999)]
def is_prime():
  return [i for i in All_4digitNumbers() if sympy.isprime(i) and i > 1487]
def Combined3_numbers():
  for i in is_prime():
    if sorted(str(i)) == sorted((str(i+3330))) == sorted(str(i+3330+3330)):
      k1 = str(i) + str(i + 3330) + str(i + 3330 + 3330)
  return k1
print(Combined3_numbers())
