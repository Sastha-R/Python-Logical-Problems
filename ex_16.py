try:

    operator = input("enter an operator:")
    
    num1 = int(input("enter a value:"))

    num2 = int(input("enter a value"))


    if operator not in ["+","-","*","/"]:
        raise ValueError("invalid operator")

    if operator == "+":
        result = num1 + num2

    elif operator == "-":
        result = num1 - num2

    elif operator == "*":
        result = num1 * num2

    elif operator == "/":
        result = num1 / num2

    print(result)

except Exception as e:
    print(e)

except ValueError as v:
    print(v)

