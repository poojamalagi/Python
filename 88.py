# Find Factorial using fun
def num(a):
    fact=1
    while a>=1:
        fact*=a
        a=a-1
    return fact

while True:

    print("\nEnter the option according to your need")
    no = int(input("1.Enter number \n2.Exit : "))

    if no == 1:
        a = int(input("Enter the value to find factorial = "))

        total = num(a)

        print(f"Factorial of {a} is {total}")

    elif no == 2:
        print("Program exited")
        break

    else:
        print("Invalid option")
