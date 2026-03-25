#  Count how many even numbers are between 1 and 100. 
count=0
for i in range(1,101):
    if i%2==0:
        count+=1
print("total count of even number = ",count)
