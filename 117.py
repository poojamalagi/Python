# Display only the first line of a file.
with open("word.txt","r") as f:
    data=f.read()
a=[]
for i in data.split("\n"):
    a.append(i)
for i in range(len(a)):
    if i ==0:
     print("Files first line is =",a[i])
  # alternative way for same  task  
# with open("word.txt", "r") as f:
#     data = f.read()

# lines = data.split("\n")
# print("First line is =", lines[0])