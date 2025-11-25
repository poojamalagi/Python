n = int(input("How many numbers? "))
sum = 0
count = 0
print("Before","Sum=",sum,"Count=",count)
for i in range(n):
    value = int(input("Enter a number: "))
    count += 1
    sum += value
print("After","Sum=",sum,"Count=",count,"Total Average=",sum/count)
