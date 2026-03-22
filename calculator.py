print("Simple Calculator")
print("Operations: + | - | * | /")

a = float(input("Enter first number: "))
op = input("Enter operation: ")
b = float(input("Enter second number: "))

if op == "+":
    print("Result:", a + b)
elif op == "-":
    print("Result:", a - b)
elif op == "*":
    print("Result:", a * b)
elif op == "/":
    print("Result:", a / b if b != 0 else "Error: Division by zero")
else:
    print("Invalid operation")
