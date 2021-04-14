#!/usr/bin/env python3

def calculate_sum_of_multiples(multiples, max_num):
  tmp_arr=[]
  for index in range(1, max_num):
    for num in multiples:
      if index%num == 0:
        tmp_arr.append(index)
        break   
  return sum(tmp_arr)

print(calculate_sum_of_multiples([3,5], 1000)) 
