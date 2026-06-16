# Write 5 numbers entered by the user into a file ( numbers.txt ), one per line.
a=[]
for i in range(5):
    a.append(int(input("enter the number")))
for i in a:
    print(i)

with open("namubers.txt","a") as f:
    for i in a:
       f.write(str(i)+"\n")