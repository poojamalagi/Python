# Create a list and:
# Add one element at the end
# Add one element at the beginning
num=[3,4,8,6,4,10,45,7,67]
newline=[0]*(len(num)+2)
newline[0]=34
for i in range(len(num)):
    newline[i+1]=num[i]
newline[(len(newline)-1)]=88
print(newline)