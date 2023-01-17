# Lists are like arrays in JS
# Lists are created similarly to variables:
# myFriends = [
#     "Chase",
#     "Morgan",
#     "Fayth"
# ]
# print(myFriends)
# Like JS, you can put anything in a list and python will be fine with it (strings, numbers, booleans)

# If you want to select a specific element from a list, you would do that similarly to JS as well.
# myFriends = [
#     "Chase",
#     "Morgan",
#     "Fayth"
# ]
# print(myFriends[0]) #Returns "Chase"
# # And you can select elements starting from the back of the list by using a negative index
# myFriends = [
#     "Chase",
#     "Morgan",
#     "Fayth"
# ]
# print(myFriends[-1]) #Returns "Fayth"
#Keep in mind that when starting from the front of the list, the first index is 0, however when starting from the back of the list, the first index is -1.

#If you want to grab sections of a list, you can do that in a couple different ways: 
# myFriends = [
#     "Chase",
#     "Morgan",
#     "Fayth"
# ]
# print(myFriends[1:]) #This returns the element specified by the index, as well as everything after. Ex: Morgan, Fayth

# myFriends = [
#     "Chase",
#     "Morgan",
#     "Fayth",
#     "Kenna",
#     "Carter",
#     "Valen"
# ]
# print(myFriends[1:4]) # This returns everything from the first specified index to the second, not including the second specified index. This example returns everything from 1 to 4, not including 4. Ex: Morgan, Fayth, Kenna

# You can also modify elements in a list:
# myFriends = [
#     "Chase",
#     "Morgan",
#     "Fayth",
#     "Kenna",
#     "Valen"
# ]
# myFriends[1] = "Jordan"
# print(myFriends) # Returns full list, with the specified index being modified to say Jordan. Ex: Chase, Jordan, Fayth, Kenna, Valen


#//////////////////////////LIST FUNCTIONS/////////////////////////////

# These are some different functions you can use with lists.
# print(): prints the list/any other stuff.
# favorite_colors = [
#     "Red",
#     "Blue",
#     "Green",
#     "Black",
#     "Purple"
# ]

# myFriends = [
#     "Chase",
#     "Morgan",
#     "Fayth"
# ]
# print(myFriends)

# extend(): Allows you to take a list and append another list.
# favorite_colors = [
#     "Red",
#     "Blue",
#     "Green",
#     "Black",
#     "Purple"
# ]

# myFriends = [
#     "Chase",
#     "Morgan",
#     "Fayth"
# ]
# myFriends.extend(favorite_colors)
# print(myFriends) # This appends/adds the list of favorite colors to the back of myFriends list.
# NOTICE: If you use extend() to add an individual element as a string, it will add it by each individual letter.

# If you are trying to add an individual element, use the append() function.

# append(): adds an individual element to the back of a list.
# favorite_colors = [
#     "Red",
#     "Blue",
#     "Green",
#     "Black",
#     "Purple"
# ]

# myFriends = [
#     "Chase",
#     "Morgan",
#     "Fayth"
# ]
# myFriends.append("Kenna")
# favorite_colors.append("Yellow")
# print(myFriends, favorite_colors)

# insert(): Inserts an element at a specified point of your list. This function takes 2 parameters. The first will be the index where you would like to insert the new element, the second will be the element you would like to insert.
# favorite_colors = [
#     "Red",
#     "Blue",
#     "Green",
#     "Black",
#     "Purple"
# ]

# myFriends = [
#     "Chase",
#     "Morgan",
#     "Fayth"
# ]
# myFriends.insert(2, "Kenna")
# favorite_colors.insert(3, "Yellow")
# print(myFriends, favorite_colors)
# This would add the specified elements at the specified index. 

# remove(): removes an element from a list. Just type in the element you would like to remove.
# favorite_colors = [
#     "Red",
#     "Blue",
#     "Green",
#     "Black",
#     "Purple"
# ]

# myFriends = [
#     "Chase",
#     "Morgan",
#     "Fayth"
# ]
# myFriends.remove("Fayth")
# favorite_colors.remove("Purple")
# print(myFriends, favorite_colors)
# This returns the lists with the specified elements removed.

# clear(): clears the entire list.
# favorite_colors = [
#     "Red",
#     "Blue",
#     "Green",
#     "Black",
#     "Purple"
# ]

# myFriends = [
#     "Chase",
#     "Morgan",
#     "Fayth"
# ]
# favorite_colors.clear()
# print(myFriends, favorite_colors)
# Now, myFriends is still the same, but the favorite_colors list is returned empty.

# pop(): pops the last element off of the list.
# favorite_colors = [
#     "Red",
#     "Blue",
#     "Green",
#     "Black",
#     "Purple"
# ]

# myFriends = [
#     "Chase",
#     "Morgan",
#     "Fayth"
# ]
# favorite_colors.pop()
# print(favorite_colors)
# The list is now returned, but without the last element. Ex: Red, Blue, Green, Black

# index(): Written in the print statement, you can check to see if a specific element is in your list.
# favorite_colors = [
#     "Red",
#     "Blue",
#     "Green",
#     "Black",
#     "Purple"
# ]

# myFriends = [
#     "Chase",
#     "Morgan",
#     "Fayth"
# ]
# print(myFriends.index("Fayth"))
# Returns 2. This will tell you that Fayth is at index 2 on the list.

# count(): Tells you how many times an element appears in a list.
# favorite_colors = [
#     "Red",
#     "Blue",
#     "Green",
#     "Black",
#     "Purple",
#     "Black",
#     "Black"
# ]

# myFriends = [
#     "Chase",
#     "Morgan",
#     "Fayth"
# ]
# print(favorite_colors.count("Black"))
# Returns 3, because Black appears in the list 3 times.

# sort(): Sorts the list in ascending/alphabetical order.
# favorite_nums = [
#     7, 
#     4, 
#     2, 
#     8, 
#     1, 
#     1423
# ]

# myFriends = [
#     "Chase",
#     "Morgan",
#     "Fayth"
# ]
# favorite_nums.sort()
# myFriends.sort()
# print(myFriends, favorite_nums)
# Lists are returned in either ascending/alphabetical order.

# reverse(): reverses the order of the list.
# favorite_colors = [
#     "Red",
#     "Blue",
#     "Green",
#     "Black",
#     "Purple"
# ]

# myFriends = [
#     "Chase",
#     "Morgan",
#     "Fayth"
# ]
# myFriends.reverse()
# favorite_colors.reverse()
# print(myFriends, favorite_colors)
# Lists are returned in reverse order.

# copy(): You can use this to make a copy of a list, and give it a new name.
# myFriends = [
#     "Chase",
#     "Morgan",
#     "Fayth"
# ]
# friendsList2 = myFriends.copy()
# print(friendsList2)
# Now friendsList2 is a second copy of myFriends

# join(): joins the elements of a list/tuple together into a string. You must specify the way you seperate the elements, ie " " for a space, "#" would put hash's in between the words, etc.
# myFriends = [
#     "Chase",
#     "Morgan",
#     "Fayth"
# ]
# print(" ".join(myFriends))
# Returns the list as a string with a space in between each element. Ex: Chase Morgan Fayth