# Question: Write a program to create, append, and remove lists in Python using NumPy.


import numpy as np

list = np.array([1, 2, 3, 4, 5])

print("Original list: {list}")


list2 = np.append(list, 6)

print("appended list:", list2)

list3 = np.delete(list, 3)
print("appended list:", list3)

