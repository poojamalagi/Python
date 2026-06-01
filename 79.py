# Count how many times an of 2 element appears.
# t = (1, 2, 2, 3, 2, 4)
t = (1, 2, 2, 3, 2, 4)
count=0
for i in range(len(t)):
    if t[i]==2:
        count+=1
print(f"2 appeares {count} times")
# print(t.count(2))