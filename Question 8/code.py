def factorial(n):
    # Base case: if n is 0 or 1, return 1
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case: n * factorial of n-1
        return n * factorial(n - 1)

# Input: number to find the factorial
num = int(input("Enter a number: "))

# Call the factorial function and print the result
print(f"The factorial of {num} is {factorial(num)}")
