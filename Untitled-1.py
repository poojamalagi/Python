a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

x1 = (-b + (pow(b, 2) - 4*a*c)**0.5) / (2*a)
x2 = (-b - (pow(b, 2) - 4*a*c)**0.5) / (2*a)

print(f"x1 = {x1}\nx2 = {x2}")