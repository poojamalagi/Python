# Sum of Numbers using Recursion
def add(n):
    """adding the n number to till 1"""
    if n==1:
        return 1
    else:
        return n+add(n-1)
a=int(input("enter the value to find the sum="))
print(f"total sum of {a}is =",add(a))