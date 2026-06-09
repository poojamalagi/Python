# Count the frequency of each character in a string.
str=input("enter the word to count the repitation of each alphabets=")
new={}
for i in str:
    if i ==" ":
        continue
    elif i in new:
        new[i]=new[i]+1
    else:
        new[i]=1
print(new)
        
    