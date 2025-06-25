#Define a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
n=int(input("Enter the number:"))
def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print("The factorial of",n,"is",factorial(n))
