
while(True):
    operand1 = int(input("enter first number = "))
    operator = input("enter operator like '+' '-' '*' '/' ")
    operand2 = int(input("enter second number = "))

    match operator:
        case '+':
            # result = operand1 + operand2
            print(operand1+operand2)
            #break

        case '-':
            result = operand1 - operand2
            print(result)
            #break

        case '*':
            result = operand1 * operand2
            print(result)
            #break

        case '/':
            result = operand1 / operand2
            print(result)
            #break

        case _:
            print("you are using invalid operator")
            #break
    
    exitGate = input("if you want to exit then type 'exit'if not then type 'no' = ")
    if(exitGate == 'exit'):
        break

