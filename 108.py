# List Index Access Ask the user to enter an index.Print the element at that index.
# ValueError if the user enters text
# IndexError if the index is not available
s=[2,33,54,33]
try:
    a=int(input("enter the index number to access the list="))
    print(s[a])
except ValueError:
    print("please enter the number")
except IndexError:
    print("entered index is not valid")