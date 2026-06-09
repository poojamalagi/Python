a=[]
n=int(input("enter the size of number"))
for i in range(n):
    a.append(int(input("enter the numbers")))
print("list",a)
print("after conversting list to tuple")
tp=tuple(a)
print(tp)