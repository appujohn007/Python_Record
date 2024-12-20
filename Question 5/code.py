# Question: Convert temperature values back and forth between Celsius (c), and Fahrenheit (f). [Formula: c/5= f-32/9] 

mode = input('Enter "C" to convert from Fahrenheit to Celsius, "F" for Celsius to Fahrenheit: ')

if mode in ["c", "C"]:
  fahrenheit = float(input("Enter your temperature value in Fahrenheit to convert. eg: 45: "))
  value = 5/9 * (fahrenheit - 32)
  print(f"{fahrenheit} Fahrenheit is {value}° Celsius")

if mode in ["f", "F"]:
  celsius = float(input("Enter your temperature value in Celsius to convert. eg: 45: "))
  value = 9/5 * celsius + 32
  print(f"{celsius}° Celsius is {value} Fahrenheit")




#Output 

Enter "C" to convert from Fahrenheit to Celsius, "F" for Celsius to Fahrenheit: F
Enter your temperature value in Celsius to convert. eg: 45: 12.78
12.78° Celsius is 55.004 Fahrenheit 
