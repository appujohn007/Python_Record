# Question: Convert temperature values back and forth between Celsius (c), and Fahrenheit (f). [Formula: c/5= f-32/9] 

mode = input('Enter "C" to convert from Fahrenheit to Celsius, "F" for Celsius to Fahrenheit: ')

if mode in [c, C]:
  fahrenheit = int(input("Enter your temperature value in Fahrenheit. eg: 45"))
  value = 5/9 * (fahrenheit - 32)
  print("{fahrenheit} Fahrenheit is {value}° Celsius")
