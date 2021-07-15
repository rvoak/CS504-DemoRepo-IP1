## File to hold utility functions

import numpy as np 

def get_random_integer():
  random_int = np.random.randint(100, size = 1)
  return random_int[0]

