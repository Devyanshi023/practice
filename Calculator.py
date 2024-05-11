def addition(x,y):
    return x+y

def substraction(x,y):
    return x-y

def multiplication(x,y):
    return x*y

def division(x,y):
    if y != 0:
        return x/y
    else:
        print("Cannot divide by 0")

def remainder(x,y):
    return x%y

def square(x):
    return x**2

def cube(x):
    return x**3

def exponent(x,y):
    return x**y

def squareroot(x):
    return x**0.5

def operation():
    print("Select the operator you want to perform.")
    print("1. Addition ")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus(Remainder)")
    print("6. Square")
    print("7. Cube")
    print("8. Exponentiation")
    print("9. Square root")

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
operation()

choice = int(input("Enter the operator number"))
if choice == 1:
    result = addition(num1,num2)
    print(num1," + ",num2,  "=" ,result)

elif choice == 2:
    result = substraction(num1,num2)
    print(num1, " - ", num2, " = ", result)

elif choice == 3:
    result = multiplication(num1,num2)
    print(num1, " * ", num2, " = ", result)

elif choice == 4:
    result = division(num1,num2)
    print(num1, " / ", num2, " = ", result)

elif choice == 5:
    result = remainder(num1,num2)
    print(num1, " % ", num2, " = ", result)

elif choice == 6:
    result = square(num1)
    result1 = square(num2)
    print("Square of ",num1, " = ", result)
    print("Square of ",num2, " = ", result1)

elif choice == 7:
    result = cube(num1)
    result1 = cube(num2)
    print("Cube of ",num1, " = ", result)
    print("Cube of ",num2, " = ", result1)

elif choice == 8:
    result = exponent(num1,num2)
    print(num1, " ** ", num2,  " = ", result)

elif choice == 9:
    result = squareroot(num1)
    result1 = squareroot(num2)
    print("Square root of ",num1, " = ", result)
    print("Square root of ",num2, " = ", result1)

else:
    print("Invalid Choice")