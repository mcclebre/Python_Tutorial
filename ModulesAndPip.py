# USES AN IMPORT OF USEFUL_TOOLS FILE


# A module is a Python file that we can import into our current Python file. You can fill a file with a bunch of useful functions, information, etc.. And then import it into your current file, and you would then have access to all of those functions and information.

# import useful_tools 

# Now after importing the file, I can use any of the functions from that useful_tools file.

import useful_tools

print(useful_tools.roll_dice(6))

# This will now run the roll_dice function from the useful_tools file, with 6 as a parameter, meaning we are rolling a 6 sided die. This function will return a random number between 1-6.

# There is a giant database of Python modules on the Python website, if you search "List of Python modules" on Google, you can select the version 3 link and it will give a FREAKIN GINORMOUS list of different modules that are already created for Python.
# There are built in modules that we already have access to, or there are external modules. When you look at a specific module from that database of Python modules, it will tell you where that module is stored.

# You can look up lots of different Python modules, and they will have installation instructions. 

# PIP: You can use pip to install Python modules, you would use pip inside of your terminal. For instance, if you want to install Python Docx, which allows you to use Python to make word documents, you can run the command "pip install python-docx" and it will install the module so that you can use it. Most third party modules will be installable using pip in your terminal, otherwise they will have specific installation instructions.
