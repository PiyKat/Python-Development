#! python3

def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

x = input("Enter value of n: ")
fact = factorial(int(x))
print(fact)
        
