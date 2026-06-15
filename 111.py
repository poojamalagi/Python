# Ask the user for their name and save it in name.txt
name=input("enter data=")
fl=open("name.txt","a")
txt=fl.write(name +"\n")
fl.close()
with open("name.txt","r") as f:
    print(f.read())