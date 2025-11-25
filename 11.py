def computepay(h, r):
    if h>40:
        reg=40*r
        extra=h-40
        pay=reg+(extra*1.5*r)
    else:
        pay=h*r
    return pay

h=float(input("Enter Hours:"))
r=float(input("enter the rate :"))
p = computepay(h, r)
print("Pay", p)