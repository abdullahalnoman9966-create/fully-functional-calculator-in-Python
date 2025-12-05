while True:
    try:
        num1 = float (input("Entre first number:"))
        num2 = float (input ("Enter second number"))
    except ValueError:
        print("only number are allowed")
        continue
    print("=" * 30)
