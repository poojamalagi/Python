# create list and handle multiple error
try:
    a=[]
    n=int(input("how many numbers you want to enter"))
    for i in range(n):
        a.append(int(input(f"enter {i+1} numbers")))
    key=int(input("enter the index number, you want to access"))
    print(a[key])
except ValueError:
    print("please enter the number")
except IndexError:
    print("entered index is not valid")