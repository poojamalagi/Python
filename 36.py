#read character and check whether is upper case if yes then convert into lower case with build in fun
while True:
  ch=input("enter the char")
  if (len(ch)==1) and (ch>='A' and ch<='Z'):
    print(ch.lower())
  else:
    print("is not upper case alaphabet or single character")
    break