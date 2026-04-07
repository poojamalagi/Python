#Print until user exits
# Keep asking user input and print it
# Stop when user enters 0

while True:
    a=input("Enter the name your fav sports")
    if(a=="0"):
        break
    name=input("Enter your name")
    print(f"{name.upper()} fav sports = {a}")
    