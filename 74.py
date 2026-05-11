# take the list from user and find the smallest number in that
n=int(input("enter the size of number"))
num=[]
for i in range(n):
    num.append(int(input("enter the number")))
smallest=num[0]
for i in range(1,n):
    if num[i]<smallest:
        smallest=num[i]
print("smallest number=",smallest)