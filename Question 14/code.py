#Question:
"""
Program to check whether the given number is a valid mobile number or not using functions.
Rules: 1. Every number should contain exactly 10 digits. 2. The first digit should be 7 or 8 or 9 
"""

def checker(num):
  if len(num) == 10:
    if num[0] in "789": 
      return "Number is valid"
    else:
      return "Invalid Number: Number Don't start with 7, 8, or 9"

  else:
    return "Invalid Number: Number Don't have 10 digits"


def main():
  num = input("Kindly enter your mobile number to check: ")
  status = checker(num)
  
  print(status)
main()
