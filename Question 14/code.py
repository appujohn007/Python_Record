#Question:
"""
Program to check whether the given number is a valid mobile number or not using functions.
Rules: 1. Every number should contain exactly 10 digits. 2. The first digit should be 7 or 8 or 9 
"""

def checker(num):
  if len(num) == 10 and num[0] in "789":
    return True 

else False


def main():
  num = input("Kindly enter your mobile number to check: ")

main()
