# Count how many lines are present in a file.
with open("word.txt","r") as f:
    data=f.read()
count=0
for i in data.split("\n"):
    count+=1
print("Total line in the given file is =",count)
    