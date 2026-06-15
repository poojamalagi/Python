# Create a file named hello.txt and write:
print("hello World")
with open("hello.txt","w") as f:
    f.write("hello word")
with open("hello.txt","r") as f:
    f.read()