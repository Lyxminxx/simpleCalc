firstNum = float(input("Enter FIRST Number: "))
type = input("choose between +, -, *, / : ")
secondNum = float(input("Enter SECOND Number: "))

if type == "+":
    print(firstNum+secondNum)
elif type == "-":
    print(firstNum-secondNum)
elif type == "*":
    print(firstNum*secondNum)
elif type == "/":
    print(firstNum/secondNum)
else:
    print("Error")