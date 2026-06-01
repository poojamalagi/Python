# Largest Number
# Create function to find largest among 3 numbers.
def lar(a,b,c):
    """using 3 number to find largest one"""
    if a>b and a>c:
        return a
    elif b>c:
        return b
    else:
        return c
a=int(input("enter the a value="))
b=int(input("enter the b value="))
c=int(input("enter the c value="))

largest=lar(a,b,c)
print(lar.__doc__)
print(f"the Largest number is={largest}")