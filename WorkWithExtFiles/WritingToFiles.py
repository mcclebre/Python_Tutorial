# IF you do not already have an external file, you can create one like this: 

# employee_file = open("employees.txt", "x")

# Lets say we have a new employee join the company, and we want to add to our employees.txt file. We can do this in a couple of ways. 
# The first is if we simply wanted to add on to our list, in which case we would use "a" mode to append our employee_file, and then instead of printing the file we would .write() to it.

# employee_file = open("employees.txt", "a")
# employee_file.write("Clim - Human Resources")
# employee_file.close()
# This will not print anything into our terminal to indicate the new line has been added, however if you check your employees.txt file, you can see the new line has been added.
# BE CAREFUL!!!!! It's easy to mess up files when editing them like this, because if you run the program multiple times, it will continue to add whatever you told Python to .write() as many times as you run the program.
# Also, if you run this program as is, it will simply add the new information onto the back of the last line of the file. If you want to put the new information on a new line, you can use the new line command refered to in WorkingWithStrings:

# employee_file = open("employees.txt", "a")
# employee_file.write("\nGrim - Mail Pit")
# employee_file.close()
# This now entered our newest mail pit employee onto a new line in our employee_file.

# You can also overwrite everything in a file by using "w" instead of "a", since you are telling Python you are wanting to write the file instead of append to it. Ex:

# employee_file = open("employees.txt", "w")
# employee_file.write("\nGrim - CEO")
# employee_file.close()
# Now, Grim worked extra hard and made his way out of the mail pit, fired everyone else, bought majority shares and took over the company.
#OBVIOUSLY, YOU NEED TO BE CAREFUL WITH THIS MODE SO YOU DONT COMPLETELY SCREW UP AN IMPORTANT FILE.