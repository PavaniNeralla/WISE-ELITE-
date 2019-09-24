import sympy
def is_prime():
  return [i for i in range(2,3940) if sympy.isprime(i)]
def prime_sum():
  k1 = 0
  for i in is_prime():
    k = sum(is_prime()) 
    k1 += i
    yield(k-k1)
def is_sum_prime():
  return [i for i in prime_sum() if sympy.isprime(i)]
is_sum_prime()[0]
