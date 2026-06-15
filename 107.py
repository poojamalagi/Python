#Division Calculator.Ask the user for two numbers.Concepts: ValueError, ZeroDivisionError
try:
    a = int(input("Enter first value: "))
    b = int(input("Enter second value: "))

    print(a / b)

except ValueError:
    print("Enter numbers, not words")

except ZeroDivisionError:
    print("Cannot divide by zero")
    

        