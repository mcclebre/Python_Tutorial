# You can create a class similarly to how you would create a list or a variable, except you will call class and then name it. Then everything you put inside the codeblock will be a part of that class.
class Student:
# You can then use an init function to define attributes that class should have, or for this example you would be defining what a "Student" is. Init functions are created like this:
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation
# Now that this class is created, we can use this class in another file. For this example we will be using this class in the Classes&Objects.py file.

# SO WHAT THE HECK IS THIS INIT FUNCTION AND WHATS HAPPENING WITH IT?
# When we create a new student object, it runs this __init__ function. This makes it so that when we pass in things like name, major, gpa, etc, it ASSIGNS THE PARAMETER THAT WE PASS INTO THIS CLASS AS AN ACTUAL ATTRIBUTE OF THE CLASS. When we pass name, gpa, etc, we are really just passing in parameters that don't specifically mean anything useful, unless we have an init function telling the class that these parameters are going to equal something. Ex:
# 
# self.name: is the name of the object, which is equal to the name parameter we pass in. 
# self.major: is the major for the object, which is equal to the major parameter we pass in. 
# 
# and so on and so forth. 
# "self" is refering to the actual object.