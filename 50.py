# Reverse a number using a for loop. 
a=int(input("enter the number="))
rev=0
for i in range(1, a+1):
    if a==0:
        break
    r=a%10
    rev=rev*10+r
    a=a//10
print("reverse=",rev)