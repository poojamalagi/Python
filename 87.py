#  Largest Number
# Create function to find largest among 3 numbers using for loop to take numbers
def lar(num):
    """using 3 number to find largest one"""
    big=num[0]
    for i in num:
      if i>big:
         big=i
    return big
num=[]
for i in range(3):
    a=int(input(f"enter the {i+1} number="))
    num.append(a)
largest=lar(num)
print("largest number in the list is =",largest)
    