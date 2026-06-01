# Function checks whether number is even or odd.
def check(a):
    """checking the number  whether it's even or odd"""
    if(a%2==0):
        return "Even"
    else:
        return "odd"
a=int(input("enter the value to check even or odd="))
c=check(a)
print(c)