#read character and check whether is upper case if yes then convert into lower case
ch=input("enter the char")
if (ch>='A' and ch<='Z'):
    ch=chr(ord(ch)+32)
    print(ch)
else:
    print(ch,"is not upper case")