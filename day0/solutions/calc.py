import cs50

first = cs50.get_float("First number: ")
operation = cs50.get_string("Operation: ")
second = cs50.get_float("Second number: ")

if operation == "+":
    print(first + second)
elif operation == "-":
    print(first - second)
elif operation == "x":
    print(first * second)
elif operation == "/":
    print(first / second)
elif operation == "^":
    print(first ** second)
else:
    print("Invalid input!")
