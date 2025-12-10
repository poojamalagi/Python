#Greeting depending on time
a=int(input("enter the timing: "))
if(a>=1 and a<12):
    print("Good Morning")
elif(a>=12 and a<16):
    print("Good Afternoon")
elif(a>=16 and a<20):
    print("Good Evening")
elif (a>=20 and a<=24):
    print("Good Night")
else:
    print("invalid number")
    