# Count vowels in a file
# Read the file.
# Count a, e, i, o, u (both uppercase and lowercase).
with open("word.txt","r") as f:
    data=f.read()
count=0
for i in data:
    if i in "AEIOUaeiou":
        count+=1
print("Total vowels in the file=",count)
