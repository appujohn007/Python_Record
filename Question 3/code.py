# Question: Write a program to create, append, and remove lists in Python using NumPy.


import numpy as np

#makes a list 
list = np.array([1, 2, 3, 4, 5])
print("Original list", list)

#add number 6 to the list
list2 = np.append(list, 6)
print("appended list:", list2)

# remove 4th indexed value 
list3 = np.delete(list, 3)
print("deleted list:", list3)



#Output 
Original list [1 2 3 4 5]
appended list: [1 2 3 4 5 6]
deleted list: [1 2 3 5] 
