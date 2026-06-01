# Find the number of unique words in a sentence:
text = "python is easy and python is powerful"
new=set(text.split())
count=0
for i in new:
    count+=1
print("total count in this text=",count)
