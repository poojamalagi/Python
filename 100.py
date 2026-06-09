# take a sentence and count alphabets, numbers and special character
wrd=input("enter the sentence=")
new={'character':0,
    'number':0,
    'special':0
}
for i in wrd:
    if (i>='A' and i<='Z') or (i>='a' and i<='z'): #or we can also write if ('A'<=i<='Z' or 'a'<=i<='z')
        # if i in new:
        new['character']=new['character']+1
        # else:
            # new[i]=1
    elif i>='0' and i<='9':
        new['number']=new['number']+1
    elif i!=" ":
        new['special']=new['special']+1
print(new)
        