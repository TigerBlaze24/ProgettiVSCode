from multiprocessing import Process
import time

def bubble_sort_v2():

  from random import randint
    
  x = [randint(0, 10000) for _ in range(50000)]
      
  ho_fatto_swap: bool = True
  for i in range(len(x)):
    for j in range(len(x) - i - 1):
      if x[j] > x[j+1]:
        #swap(x[j], x[j+1])
        ho_fatto_swap = False
        temp: int = x[j]
        x[j] = x[j+1]
        x[j+1] = temp
    if ho_fatto_swap:
      break