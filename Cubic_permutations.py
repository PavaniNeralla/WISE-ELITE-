def max_digit_sum():
  return max([digit_sum(a ** b) for a in range(1,101) for b in range(1,101)])
def digit_sum(n):
  return sum([int(i) for i in str(n)])
max_digit_sum()
