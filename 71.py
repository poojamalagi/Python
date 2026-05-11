# Print numbers between 2 and 5 and even and store it
a = [6, 1, 4, 2, 5, 3,8,10,12]
store=[]
for i in a:
    if ((i>2 and i<=12) and i%2==0):
        store.append(i)
print(store)
    