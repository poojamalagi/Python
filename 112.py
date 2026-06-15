# Count the number of characters in a file.
with open("name.txt","r") as f:
    data=f.read()
print("file content")
print(data)
count=0
for i in (data):
      count+=1
print("Total character=",count)
