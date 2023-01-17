# While loops can be used to loop through a section of code as long as a condition is true, and then it would exit as soon as that condition was false. 
i = 1
while i <= 10:
    print(i)
    # For this example we are incrementing i. You can do this by setting the variable of i = i + 1, or you can use the shorthand i += 1. This is Pythons version of i++(JS)
    i += 1
# Once i = 10, it will stop looping, and continue on to the rest of the code.
print("Done with loop")
