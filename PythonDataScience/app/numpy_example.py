"""
Here's our first look at "Why NumPy?" - SPEED!
NumPy performs operations on entire datasets at once, without loops.
This superpower is called "vectorization"

This cleans up your code, and makes your operations significantly faster.
The bigger the dataset, the more dramatic the difference.

Also, we're importing the time module to measure how long our operations take
"""
import time
import numpy as np


plain_list = list(range(10_000_000))
numpy_array = np.array(plain_list)

# Time how long it takes to loop through the plain list
start = time.time()
result = [x * 2 for x in plain_list]
plain_list_time = time.time() - start

# NumPy Vectorized Operation
start = time.time()
result = numpy_array * 2 # every element multiplied by 2 like in the python list
numpy_array_time = time.time() - start

print(f"Plain list took {plain_list_time:.6f} seconds to multiply each element by 2")
print(f"Numpy Array took {numpy_array_time:.6f} seconds to multiple each element by 2")

print("=============(More Realistic Application of NumPy - Business Calculations)")

#Hypothetical sales data for January

january_sales = np.array([
    120, 135, 98, 142, 167, 88, 95,
    201, 178, 156, 134, 189, 145, 112,
    167, 198, 223, 145, 167, 134, 189,
    201, 178, 156, 134, 189, 145, 112,
    167, 198, 223
])

