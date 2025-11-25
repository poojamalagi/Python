hrs = input("Enter Hours:")
h = float(hrs)
rate=float(input("enter normal rate"))
r=1.5
if h<=40:
    pay=h*rate
   
else:
    overtime=h-40
    regular=40*rate
    pay=regular+(overtime*r*rate)
print(pay)
    
