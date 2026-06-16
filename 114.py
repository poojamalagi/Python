#  Read all numbers from numbers.txt and calculate their sum.
with open("namubers.txt","r") as f:
    rst=f.read()
print(rst)
sum=0
for i in rst.split():
    sum+=int(i)     
    print(i)
print("total sum =", sum)
with open("namubers.txt","a") as f:
    f.write(f"total sum={sum}")
