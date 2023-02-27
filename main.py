#add
def add(n1, n2):
    return n1 + n2

#Subtract
def subtract(n1,n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1 / n2

operation = {
             "+": "add",
             "-": "subtract",
             "*": "multiply",
             "/": "divide"
}

def calculator():
    num1 = float(input("what's the first number?: "))

    is_answer = False
    while not is_answer:
        for symbol in operation:
            print(symbol)
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("what's the next number?: "))

        if operation_symbol == "+":
            answer = add(num1, num2)
        elif operation_symbol == "-":
            answer = subtract(num1, num2)
        elif operation_symbol == "*":
            answer = multiply(num1, num2)
        elif operation_symbol == "/":
            answer = divide(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        type = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ")
        if type == "y":
            num1 = answer
        elif type == "n":
            is_answer = True
            print(answer)
            calculator()

calculator()
