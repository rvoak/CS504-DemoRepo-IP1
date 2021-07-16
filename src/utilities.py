## File to hold utility functions

import numpy as np 

def get_random_integer():
  random_int = np.random.randint(100, size = 1)
  return random_int[0]
  
def get_random_integer_array(upper_bound = 100, arr_size = 10):
  random_ints = np.random.randint(upper_bound, size = arr_size)
  return random_ints

