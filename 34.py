#read 4 number and find the smallest number in that
a=int(input("enter the number="))
b=int(input("enter the number="))
c=int(input("enter the number="))
d=int(input("enter the number="))
if a<b and a<c and a<d:
    print(a,"is the smallest")
elif b<c and b<d:
    print(b,"is the smallest")
elif c<d:
    print(c,"is the smaillest")
else:
    print(d,"is the smallest")