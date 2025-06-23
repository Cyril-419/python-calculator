# function to add two numbers
def add(a, b):
    return a + b
# function to subtract two numbers
def subtract(a, b):
    return a - b
# function to multiply two numbers
def multiply(a, b):
    return a * b
# function to divide two numbers
def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b
# function to raise a to the power of b
def exponent(a, b):
    return a ** b
# function to find the remainder of a divided by b
def modulus(a, b):
    return a % b
# use a loop so the calculator keeps running until the user wants to quit
while True:
# display menu options for the user to choose from
    print("\nWelcome to your Calculator,YES!")
    print("Please choose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponent (Power)")
    print("6. Modulus (Remainder)")
    print("7. Exit")
# ask the user to enter a choice
    choice = input("Enter your choice (1-7): ")
# if the user picks 7, we break the loop and end the program
    if choice == '7':
        print("Thank you for using the calculator. Goodbye!")
        break
#if user enters an invalid option (not 1-6), show error and restart loop
    if choice not in ['1', '2', '3', '4', '5', '6']:
        print("Invalid choice. Please try again.")
        continue
# this will restart the loop
# now we ask for the two numbers
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
# if user enters something thats not a number, show error and restart loop
        print("Invalid input. Please enter numbers only.")
        continue
# based on the user's choice, we call the appropriate function
    if choice == '1':
        result = add(num1, num2)
    elif choice == '2':
        result = subtract(num1, num2)
    elif choice == '3':
        result = multiply(num1, num2)
    elif choice == '4':
        result = divide(num1, num2)
    elif choice == '5':
        result = exponent(num1, num2)
    elif choice == '6':
        result = modulus(num1, num2)
#now we print the result to the user
    print(f"The result is: {result}")
#this for calling functions manually
print("\nManual function calls:")
x = 10
y = 5
print(f"add({x}, {y} = {add(x, y)}")
print(f"subtract({x}, {y}) = {subtract(x, y)}")
print(f"multiply({x}, {y}) = {multiply(x, y)}")
print(f"divide({x}, {y}) = {divide(x, y)}")
print(f"exponent({x}, {y}) = {exponent(x, y)}")
print(f"modulus({x}, {y}) = {modulus(x, y)}")
#sanity check
while True:
    choice = input("Enter something: ")
    if choice == 'exit':
        print("Bye!")
        break
    print(f"You typed: {choice}")