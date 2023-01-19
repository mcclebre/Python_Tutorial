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

# I can also create functions that we can use within a class, that can modify or give specific information about a class. I already (kind of) have an example in the Classes&Objects.py file, where I was checking if a student was on probation or not. Here is another example that is a little bit different though:
 
    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False

# This is a small function, but it determines whether or not students are on the honor roll (have a gpa greater than 3.5). Now, we have an additional function for the class, that can be used by the objects. So now you could just print(student1.on_honor_roll()) and it will return True or False. You could technically do the same thing by individual Student object, however this allows us to have one single function that we can use on any object of this class and it will run.

# The rest of this example (calling this on_honor_roll function for a student) in the Classes&Objects.py file.

# Another thing to note, but these are all going to be within the same Student class, however because of the notation it's a little hard to visualize that, so here is a pseudo-coded view of how the entire class would look altogether:

# class Student:
#    def __init__(self, name, major, gpa, is_on_probation):
#        self.name = name
#        self.major = major
#        self.gpa = gpa
#        self.is_on_probation = is_on_probation
#
#
#    def on_honor_roll(self):
#        if self.gpa >= 3.5:
#            return True
#        else:
#            return False