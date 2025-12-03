


def add(a,b):
    return a+b
def subt(a,b):
    return a-b
def multiply(a,b):                                              
    return a*b
def devide(a,b):
    if b==0:
        return "can not devide by zero"
    return a/b


def show_menu():
    print("=" * 30)
    print("Basic Calculator")
    print("=" * 40)
    print("press 1.add")
    print("press 2.subtract")
    print("press 3.multiply")
    print("press 4.division")
    print("press 5.exit")
    print("=" * 30)
show_menu()

while True:
    choice =input ("Enter your choice (1-5):")
    if choice not in ["1","2","3","4","5"]:
        print("Invalid input. plice chice 1-5")
        continue
    if choice == "5":
        print("Thank you for using the calculator")
        break

    try:
        num1 = float (input("Entre first number:"))
        num2 = float (input ("Enter second number"))
    except ValueError:
        print("only number are allowed")
        continue
    print("=" * 30)

    if choice == "1":
        print(f"addition result: {num1} + {num2} = {add(num1,num2)}")
    elif choice == "2":
        print(f"subtraction result: {num1} - {num2} = {subt(num1, num2)}")
    elif choice == "3":
        print(f"multiply result: {num1} * {num2} = {multiply (num1,num2)}")
    elif choice =="4":
        print(f"division result: {num1} / {num2} = {devide (num1, num2)}")


        

    
          

    




    