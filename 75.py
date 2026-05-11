# take list from user and find the first and second largest number
n=int(input("enter the number size"))
a=[]
for i in range(n):
    a.append(int(input("enter the number")))
big=a[0]
for i in range(1,len(a)):
    if a[i]>big:
        big=a[i]
seclargest=a[0]
for i in range(1,len(a)):
    if a[i]<big and a[i]!=big and a[i]>seclargest:
        seclargest=a[i]
    
print("first Largest number=",big)
print("Second largest number=",seclargest)
        