# Read a text file and count the total number of words.
with open("word.txt","a") as f:
    f.write("\n"+"But need some practice")
with open("word.txt","r") as f:
    data=f.read()
print(data)
count=0
for i in data.split():
    count+=1
print("Total words=",count)