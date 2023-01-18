# You can use the read command to work with external files outside of Python. 
# The first thing you need to do is open the file you want Python to work with. Do this by using the open() function, and in the functions parameters you can set two parameters. The first is the name of the file you would like to work with, the second is telling Python what you want to do with the file ("x" = Create, "r" = Read, "w" = Write, "a" = Append(you can add to this file but you cannot change any existing info), and "r+" = Read and Write)
# Generally, you are going to want to store your open function in a variable.

# employee_file = open("employees.txt", "r")

# Make sure that once you open the file, you are also closing it at some point: 

# employee_file = open("employees.txt", "r")
# employee_file.close()

# Before working with the file, you can check to see if the file is readable with the readable() function:

# employee_file = open("employees.txt", "r")
# print(employee_file.readable())
# employee_file.close()

# This will return True, because we are in read mode. If we had selected "w" or "a", it would return False, since we are not in read mode.

# There are a few functions you can use on the employee_file to get information from it:

# read():
# employee_file = open("employees.txt", "r")
# print(employee_file.read())
# employee_file.close()
# This will print out the entire employees.txt file.

# readline():
# employee_file = open("employees.txt", "r")
# print(employee_file.readline())
# print(employee_file.readline())
# employee_file.close()
# This will read the first line of the file, then moves down to the next line. If there were multiple prints with readline(), it would print each line one by one as many times as you have readline()'s.

# readlines(): 
# employee_file = open("employees.txt", "r")
# print(employee_file.readlines()[3])
# employee_file.close()
# This is a better way to read individual lines, and it prints each line as an element in a list. This allows you to access a specific line in the file using its index.

# You can also use the readlines() function in a for loop:
# employee_file = open("employees.txt", "r")
# for employee in employee_file.readlines():
#     print(employee)
# employee_file.close()
# This will loop through the employee_file list that is created with the readlines() function, and lists them out as individual lines outside of a list.
