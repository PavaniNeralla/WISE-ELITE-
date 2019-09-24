def Sum_of_powers():
  return [i ** i for i in range(1,1000)]
def last_10Digits():
  return str(sum(Sum_of_powers()))[-10: ]
last_10Digits()
