# Question: Program to construct patterns of stars (*), using a nested for loop.  HINT: Nested loop is a programming concept where a loop is placed inside a loop

n = int(input("Enter Number of rows to be shown: "))

for i in range(1, n+1):
  for j in range(1, i+1):
    print("*", end=" ")
  print()


#Output 

Enter Number of rows to be shown: 6
*
* *
* * *
* * * *
* * * * *
* * * * * * 
