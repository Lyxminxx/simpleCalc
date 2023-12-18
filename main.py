while True:
    firstNum = float(input("Enter FIRST Number: "))
    type = input("choose between +, -, *, / : ")
    secondNum = float(input("Enter SECOND Number: "))
    if type == "+":
        print(firstNum+secondNum)
        input("Click ENTER to continue: ")
    elif type == "-":
        print(firstNum-secondNum)
        input("Click ENTER to continue: ")
    elif type == "*":
        print(firstNum*secondNum)
        input("Click ENTER to continue: ")
    elif type == "/":
        print(firstNum/secondNum)
        input("Click ENTER to continue: ")
    else:
        print("Error")
        input("Click ENTER to continue: ")