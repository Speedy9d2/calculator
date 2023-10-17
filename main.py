def add(n1,n2):
 return n1 + n2

def subtract(n1,n2):
 return n1 - n2

def divide(n1,n2):
 return n1 / n2

def multiply(n1,n2):
 return n1 * n2

operator = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    num1 = float(input("What's the first number?: "))
    for option in operator:
        print(option)
    shouldContinue = True

    while shouldContinue:
        pickedOperator = input("Pick an operator: ")
        nextNum = float(input("What's the next number?: "))
        function = operator[pickedOperator]
        answer = function(num1, nextNum)
        print(f"{num1} {pickedOperator} {nextNum} = {answer}")

        if input("To continue enter Y or N  to end ") == "y":
            num1 = answer
        else: 
            shouldContinue = False
            calculator()
            
calculator()
