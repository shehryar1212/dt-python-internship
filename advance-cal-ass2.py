import sympy as sp
import random

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Can't divide by zero."

def modulus(a, b):
    return a % b

def derivative(f):
    x = sp.Symbol('x')
    der = sp.diff(f, x)
    return der

def integral(f):
    x = sp.Symbol('x')
    intg = sp.integrate(f, x)
    return intg

def roll_dice():
    input("Press ENTER to roll the dice")
    return random.randint(1, 6)

def advance_calculator(tries):
    while tries > 0:
        print(f"\nYou have {tries} tries remaining.")
        print("\nSelect operation:")
        print("1-Add")
        print("2-Subtract")
        print("3-Multiply")
        print("4-Divide")
        print("5-Modulus")
        print("6-Derivative")
        print("7-Integral")
        print("8-Exit")

        choice = input("Choose from (1-2-3-4-5-6-7-8): ")

        if choice == '8':
            print("Thank you for using the advanced calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4', '5']:
            num1 = float(input("Enter 1st number: "))
            num2 = float(input("Enter 2nd number: "))

            if choice == '1':
                print(f"The result of addition is: {add(num1, num2)}")
            elif choice == '2':
                print(f"The result of subtraction is: {sub(num1, num2)}")
            elif choice == '3':
                print(f"The result of multiplication is: {mul(num1, num2)}")
            elif choice == '4':
                print(f"The result of division is: {div(num1, num2)}")
            elif choice == '5':
                print(f"The result of modulus is: {modulus(num1, num2)}")
        
        elif choice == '6':
            f = input("Enter the equation with respect to x: ")
            try:
                function = sp.sympify(f)  
                print(f"The derivative of {f} is:\n{derivative(function)}")
            except Exception as e:
                print(f"Error in calculating derivative: {e}")

        elif choice == '7':
            f = input("Enter the equation with respect to x: ")
            try:
                function = sp.sympify(f)  
                print(f"The integral of {f} is:\n{integral(function)}")
            except Exception as e:
                print(f"Error in calculating integral: {e}")

        else:
            print("Invalid input. Please select a valid operation.")
        
        tries -= 1

        if tries > 0:
            print(f"\n{tries} calculation tries remaining!")
        else:
            print("OOPS! You have used all your calculation tries.")

def main():
    print("WELCOME DECENTRALIZED TECHNOLOGIES INTERNS")
    
    print("Please roll the dice to begin.")
    
    while True:
        points = roll_dice()
        print(f"\n Woah!, You got {points} points to start off.")
        advance_calculator(points)
        
        retry = input("\nDo you want to roll the dice and start again? (yes/no): ").lower()
        if retry != 'yes':
            print("Thank you for using the calculator. Goodbye!")
            break

main()
