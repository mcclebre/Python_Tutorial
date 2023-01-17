 # A tuple is a type of data structure, or a container where we can store different values.
 # A tuple has a key difference from a list: 
 # Tuples are immutable, meaning it cannot be changed or modified. 
 

# You can create a tuple as demonstrated below. It is set up like a list, however you use standard ()'s rather than []'s
# Tuples are indexed starting at 0.
# coordinates = (4, 5)
# print(coordinates[0]) # Returns 4

# Like stated above, you cannot modify a tuple. Ex:
# coordinates = (4, 5)
# coordinates[1] = 17
# print(coordinates[0]) # When run, this gives you an error (TypeError: 'tuple' object does not support item assignment) because you are not allowed to change or modify the tuple.

# You CAN create a list of tuples. Ex:
# coordinates = [
#     (4, 5), 
#     (6, 7),
#     (80, 34)
# ] 
# print(coordinates[0])
# This would now print the tuple that is set at index 0, returning (4, 5).