# Sum of numbers
# Keep taking numbers
# Add them to total
# Stop when user enters 0
# Print total sum
total=0
while True:
    a=int(input("enter the number"))
    if (a==0):
        break
    total+=a
print("Total sum of the number=",total)