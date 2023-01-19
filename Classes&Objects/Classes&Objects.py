# Not all data can be represented by strings, numbers, booleans, etc. This is a good opportunity to use classes and objects.
# Class: Defines your own data type.
# Object: The data type that we defined, that we can now use. Kinda confusing, but it makes more sense as you read on below.

# In our Student.py file, we created a class defining what a Student is. We will now create a Student object, which will be a "Student".
# So a class defines what an object should be, and an object is the actual thing that we have defined, that we can now use in our program.

#Now, from the Student file, we want to import the Student class.
from Student import Student

# We can now create our object, which is just like making a variable:
student1 = Student("Jim", "Business", 3.2, False)
# Because we already defined what a Student "is" with our Student class in the other file, we just need to pass on the different bits of info that we specified when we created the class (name, major, gpa, is_on_probation)

# Now, because we have defined what a Student is and created a Student object, we can access the different bits of information by printing or returning the student1 object, and specifying what information we want to get about that object.
print(student1.name) # This will return the name that we have given student1 (Jim)
print(student1.gpa) # This will return the gpa that we have given student1 (3.2)

# Now we have created the Student data type, and we can create as many objects as we want and use that object throughout our code.

student2 = Student("Pam", "Cultural Studies", 3.8, True)

def check_probation():
    if student1.is_on_probation == True and student2.is_on_probation == True:
        print("All students are on probation. How sad...")
    elif student1.is_on_probation == True and student2.is_on_probation == False:
        print( student1.name + " is on probation. Epic Fail")
    elif student1.is_on_probation == False and student2.is_on_probation == True:
        print( student2.name + " is on probation. Poor student.")
    else: 
        print("No students on probation. HOORAY!")

print(check_probation())

# Also, I just want to point out that I feel like an absolute freaking genius because I wrote that whole check_probation function by myself with no help and I freaking LOVE Python. This is fun as crap.

# Below is the rest of the example from writing an additonal class function, that applies globally to all objects of the class.
student3 = Student("Oscar Meyer", "Accounting", 3.3, False)
student4 = Student("Pim Jam", "Counseling", 2.9, True)


print(student3.on_honor_roll())