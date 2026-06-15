a=input("enter the value")
if a=="quite":
    print("program completed")
elif not a.isdigit():
    raise ValueError("please enter the value")
elif int(a)<5 or int(a)>9:
    raise ValueError("please enter the value b/w 5 to 9")