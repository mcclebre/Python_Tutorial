# You can use try except blocks to handle errors. This allows you to tell Python that if there is an error you want it to do something else, rather than have it completely break your code. This is going to be similar to try catch blocks in JS.

# number = int(input("Enter a number: "))
# print(number)

# This little program works as long as the user enters a number. If they enter another value though, it breaks and displays the error in the terminal, but does not allow Python to read past that point and will not print anything. Here is how we can fix that:

# try:
#     number = int(input("Enter a number: "))
#     print(number)
# except:
#     print("Invalid Input")

# Now, because we used try except, the invalid input of something like a string doesn't break our code, and just returns the string "Invalid Input". 
# Right now, our except statement is very broad, and will catch any error that we have in our try block, and throw the "Invalid Input" string back at you, even if your input was valid. Ex:

# try:
#     value = 10 / 0
#     number = int(input("Enter a number: "))
#     print(number)
# except:
#     print("Invalid Input")

# Because it is impossible to divide 10 by 0, Python recognizes that this is an error and throws "Invalid Input" even if the value you input was valid. The fix to this is to clarify your exception with Python, by specifying what error you want it to catch. Ex:

# try:
#     value = 10 / 0
#     number = int(input("Enter a number: "))
#     print(number)
# except ZeroDivisionError:
#     print("Divided by zero")
# except ValueError:
#     print("Invalid Input") 

# Now, when this is run it throws the error "Divided by zero" so that we know the error was caused by this impossible division. If we fix the impossible division, we can then enter a number, so on and so forth.

# One last thing we can do is we can store the error as a variable:
 
# try:
#     number = int(input("Enter a number: "))
#     print(number)
# except ZeroDivisionError as err:
#     print(err)
# except ValueError as value_err:
#     print(value_err) 

# Best practice for Python is going to be to specify your exceptions, instead of just saying except: and excepting any error, so that you know exactly what is causing issues on long code blocks.






