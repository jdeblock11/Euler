#!/usr/bin/env python3

def calculate_fib_even_sum():
  fib_arr=[0,1]
  even_arr=[]
  fib=0
  while(fib < 4000000):
    fib = sum(fib_arr[-2:])
    fib_arr.append(fib)
    if fib%2 == 0:
      even_arr.append(fib)

  return sum(even_arr)

print(calculate_fib_even_sum())
