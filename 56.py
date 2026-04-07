# Even numbers only
# Take numbers continuously
# If number is odd → skip using continue
# If even → print it
#  Stop when user enters -1
while True:
    a=int(input("enter the number"))
    if a==-1:
        break
    elif a%2!=0:
        continue
    else:
        print("Given number is even =",a)
