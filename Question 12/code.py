#Question
"""
A program that accepts the lengths of three sides of a triangle as inputs. 
The program should output whether or not the triangle is a right triangle (Recall from the Pythagorean Theorem that in a right triangle, the square of one side equals the sum of the squares of the other two sides). 
Implement using functions
"""

import math 

def check(largeside, len2, len3):
  if largeside **2 == math.sqrt((len2**2 + len3**2)):
    return True
  else:
    return False


def main():
  len1 = int(input("Enter Length of 1st side: "))
  len2 = int(input("Enter Length of 1st side: "))
  len3 = int(input("Enter Length of 1st side: "))
  largeside = max(len1, len2, len3)
  print(largeside)
  
  if check(largeside, len2, len3):
    print(f"The triangle with sides {len1}, {len2}, {len3} is right angled")
  else:
    print(f"The triangle with sides {len1}, {len2}, {len3} is not right angled") 



main()
