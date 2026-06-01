def add(a, b):
    """Adds two numbers"""
    
    return a + b
a=int(input("enter the value of a="))
b=int(input("enter the value of b="))
c=add(a,b)
print(c)
print(add.__doc__)