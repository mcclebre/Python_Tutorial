# ////////////////////BASIC A** CALCULATOR///////////////////////////
# num1 = input("Please enter a number: ")
# num2 = input("Please enter another number: ")
# result = num1 + num2
# print(result)
# This would work in theory, however by default python reads inputs as strings, so the returned result would be 78. In order to get the correct answer, you must conver the inputed value to be a number, rather than a string.

# There are 2 python functions you can use to do this. 
# int(): converts the variable into an integer number (whole number, no decimals).  
# num1 = input("Please enter a number: ")
# num2 = input("Please enter another number: ")
# result = int(num1) + int(num2)
# print(result)
# This works for whole numbers only, if you want to use decimals, you need to use another function.
# float(): This does the same thing, but allows you to use decimal numbers.
# num1 = input("Please enter a number: ")
# num2 = input("Please enter another number: ")
# result = float(num1) + float(num2)
# print(result)


#///////////////////////CALCULATOR BUT BETTER////////////////////////


def cool_calculator():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Enter an operator(+, -, /, or *): ")


    if operation == "*":
        print(num1 * num2)
    elif operation == "/":
        print(num1 / num2)
    elif operation == "+":
        print(num1 + num2)
    elif operation == "-":
        print(num1 - num2)
    else:
        print("Error: Invalid Operator Selected") 

cool_calculator()

