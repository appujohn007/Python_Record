# Question: Simple desktop calculator using Python. Only the five basic arithmetic operators.





num1 = int(input("Enter Your 1st number to calculate: "))
num2 = int(input("Enter Your 2st number to calculate: "))
opr = input("Enter Your mathematical operator for calculation. \n eg (+, -, *, /, %): ")

if opr == "+":
  result = num1 + num2

elif opr == "-":
  result = num1 - num2

elif opr == "*":
  result = num1 * num2

elif opr == "/":
  if num2 != 0:
    result = num1 / num2
  else:
    print("Division by zero not permitted...!")

elif opr == "%":
  if num2 != 0:
    result = num1 % num2
  else:
    print("Division by zero not permitted...!")

else:
  print("Invalid operator passed...!")

print(f"result: {result}")



#Output
"""
Enter Your 1st number to calculate: 23
Enter Your 2st number to calculate: 5
Enter Your mathematical operator for calculation.
 eg (+, -, *, /): +
result: 28
"""
