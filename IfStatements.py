# If statements in Python are very similar to JS, with a couple differences in syntax. Syntax for if statements are: if, elif, and else, and rather than using (){} to specify your parameter and return, you would just type what your if is, and follow it with a colon (:) to begin your return for that if.
# Another important thing to note is that rather than using & for and or || for or, you can just use "and" or "or", and if you want to say check if something is not met, rather that using !, you just say 
# not() and fill the parameter with the condition that you want to check is not met. BE AWARE THAT YOU WILL STILL USE != FOR COMPARISONS. PYTHON IS COOL AND READABLE AF BOI

# is_male = True

# if is_male:
#     print("You are a male")
# Returns "You are a male"

# is_male = False

# if is_male:
#     print("You are a male")
# else:
#     print("You are not a male")
# Returns "You are not a male"

# is_male = False
# is_tall = True

# if is_male or is_tall:
#     print("You are a male, or you are tall, or both")
# else:
#     print("You are not a male or tall")
# Returns the first print if either of the parameters are met, if both are not met, it returns the second print.

# is_male = True
# is_tall = True

# if is_male and is_tall:
#     print("You are a male and you are tall")
# else:
#     print("You are not a male or you are not tall")
# Returns first print if both of the parameters are met. If one neither are met, it returns the second print.

# is_male = False
# is_tall = True

# if is_male or is_tall:
#     print("You are a tall male")
# elif is_male and not(is_tall):
#     print("You are male, but you are short as hell.")
# elif not(is_male) and is_tall:
#     print("You are not a male but you are tall")
# else:
#     print("You are neither a male nor tall")

#////////////////////Comparisons in if statments//////////////////////
# You can compare things in a few different ways, and this process is the same as JS. == is equal to, >= is greater than or equal to, etc.

# def big_num(num1, num2, num3):
#     if num1 >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2 >= num3:
#         return num2
#     else:
#         return num3

# print(big_num(4,87,23))
# # Returns 87

# def is_dog(word):
#     if word == "dog":
#         return word
#     else: 
#         return "Not a dog bro"

# print(is_dog("cat"))
# # Returns "Not a dog bro"