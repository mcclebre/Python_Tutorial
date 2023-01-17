# When working with strings, you can use some commands to do different things to the string. 

# print("Hex\nEffect") 
# This (\n) adds a new line to your string, making it render as 
# Hex
# Effect rather than Hex Effect.

# print("Hex\"Effect")
# Using \" tells python you want to print the quotation literally, meaning it would return as Hex"Effect. If you want to add quotations or apotrophes in a string, this is how you would do so.

phrase = "Hex Effect"
# print(phrase + " is cool")
#You can set strings as a variable, and call it with its name. Like JS, you can also concatenate things when you print or return them.

# Common string functions:
# print(phrase.lower()) # Makes entire string lowercase
# print(phrase.upper()) # MAKES ENTIRE STRING UPPERCASE
# print(phrase.isupper()) # Checks if everything in the string is uppercase, and returns a boolean.
# print(phrase.upper().isupper()) # You can run multiple functions on top of each other like this ^^.
# Notice that the function 'isupper' is not in camel case, unlike how a function would be written in JS.

# print(len(phrase)) #This returns the length of the string, telling us there are 10 characters in the string "Hex Effect"

# You can grab a specific character at a specific index like this: 
# print(phrase[2]) #This would return 'x', which is the 2nd index of the string.

# You can figure out where a specific value is located in a string:
# print(phrase.index("E")) 
# print(phrase.index("Effect"))
# Both examples above would return 4, since "E" is at the 4th index and when searching for a whole word or part of a string, the word also starts at the 4th index.

#You can use the .replace function to replace the value specified as the first parameter, with whatever you specify as the second parameter. Ex:
# print(phrase.replace("Effect", "Is Cool"))
# Effect would now be replaced with Is Cool, with the final print reading "Hex Is Cool"