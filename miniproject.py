# Mini Project 1: Even & Odd Separator
# Goal:
# From a list, create:
# one list for even numbers
# one list for odd numbers
a = [1, 2, 3, 4, 5, 6, 7]
even=[]
odd=[]
for i in a:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("even=",even)
print("odd=",odd)
    