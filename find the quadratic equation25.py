#find the quadratic equation
a=int(input("enter the value of a="))
b=int(input("enter the value of b="))
c=int(input("enter the value of c="))
x1=(-b+(pow(b,2)-4*a*c)**0.5)/(2*a)
x2=(-b-(pow(b,2)-4*a*c)**0.5)/(2*a)
print("x1=",x1,"\nx2=",x2)