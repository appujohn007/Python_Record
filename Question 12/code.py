#Question
"""
A program that accepts the lengths of three sides of a triangle as inputs. 
The program should output whether or not the triangle is a right triangle (Recall from the Pythagorean Theorem that in a right triangle, the square of one side equals the sum of the squares of the other two sides). 
Implement using functions
"""

import math 

def check(len1, len2, len3):
  sides = sorted([len1, len2, len3])
  if sides[2] **2 == sides[1] **2 + sides[0] **2:
    return True
  else:
    return False


def main():
  len1 = int(input("Enter Length of 1st side: "))
  len2 = int(input("Enter Length of 1st side: "))
  len3 = int(input("Enter Length of 1st side: "))
  
  
  if check(len1, len2, len3):
    print(f"The triangle with sides {len1}, {len2}, {len3} is right angled")
  else:
    print(f"The triangle with sides {len1}, {len2}, {len3} is not right angled") 



main()


#Output 
Enter Length of 1st side: 3
Enter Length of 1st side: 4
Enter Length of 1st side: 5
The triangle with sides 3, 4, 5 is right angled
