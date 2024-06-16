'''                           SIMPLE CALCULATOR 
Topics Covered: Variables and Data Types, Control Flow and Loops, Functions

Description: Create a simple calculator that can perform basic arithmetic operations like
addition, subtraction, multiplication, and division. Use functions to handle each operation and
control flow to manage user input.'''


def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b

print("Select the Operation You Want To Perform")
print("1. ADD")
print("2. SUBSTRACT")
print("3. DIVIDE")
print("4. MULTIPLY")

while True : 
    choice = input("Enter The Given Choice (1/2/3/4) : ")

    if choice in ('1', '2', '3', '4'):
        try :
            a = float(input("Enter the 1st Value : "))
            b = float(input("Enter the 2nd Value : "))
        except ValueError:
            print("Invalid Input. Please Enter a NUMBER.")
            continue

        if choice == '1':
            print(a, " + ", b ," = ", add(a, b))
        elif choice == '2':
            print(a, " - ", b ," = ", subtract(a, b))
        elif choice == '3':
            print(a, " / ", b ," = ", divide(a, b))
        elif choice == '4':
            print(a, " * ", b ," = ", multiply(a, b))

        # To Check if the USER wants another CALCULATIONS
        # BREAK the loop if ANSWER is NO

        next_calculate = input("Let's do Another Calculation ? ") 

        if next_calculate == "Yes" :
            continue
        elif next_calculate == "No":
            break
        else:
            print("INVALID INPUT")

            