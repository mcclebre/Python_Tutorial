# For loops are used for the same thing you would use them for in JS.
# They are written a little bit differently in Python than in JS.

# for letter in "Hex Effect":
#     print(letter)
# This goes through and prints out each letter of Hex Effect.

# friends = ["Chase", "Morgan", "Kenna", "Valen"]
# for friend in friends:
#     print(friend)
# Returns each name in the friends array.

# The variable friend is given by you and can be called anything you want. Because you are telling Python to loop through the friends array, whatever you name the variable, will be considered one single iteration of the array. Ex:
# friends = ["Chase", "Morgan", "Kenna", "Valen"]
# for bingBong in friends:
#     print(bingBong)
#This still returns each name in the friends array.

#You can also loop through a collection of numbers using range(). This will loop through until it reaches the specified number.
# for index in range(15):
#     print(index)
# This will print starting from one, and go until it reaches 15, so it will print every number from 1 to 15, not including 15.

# You can also specify the range with two parameters.
# for index in range(4, 15):
#     print(index)
# This will print starting at 4 and going up to 15, not including 15.

# You can also loop the length of an array. However, instead of using friends.length(JS) you would just use len(friends) to specify you want to loop through the length of the friends array. len(friends) would return 4, so the for loop would loop 4 times through the length of the array.
# friends = ["Chase", "Morgan", "Kenna", "Valen"]
# for index in range(len(friends)):
#     print(index)
#     print(friends[index])
# You can then get returned information in a couple of ways. If you print just index, because you are telling Python to loop through the length of the array, it will return a numerical count of the indexes in the friends array. 
#HOWEVER, if you print friends[index], you are telling Python to print the element in friends, at the index the loop is on. 
# print(index): returns 0,1,2,3
# print(friends[index]): returns Chase, Morgan, Kenna, Valen 

# Like for loops in JS, you can have the loop do fun stuff:
# for index in range(5):
#     if index == 0:
#         print("Im in first boyo")
#     else:
#         print("Im not in first mano")
# This will print the first iteration as Im in first boyo, and every other iteration following would print Im not in first mano.


#///////////////CREATING EXPONENT FUNCTION W FOR LOOPS////////////////
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num

    return result
    
print(raise_to_power(3, 5))

# raise_to_power explanation: We want the function to have two parameters, one being our number that we want to raise(base_num), and the other being the number we want to raise it by(pow_num). We then need to set the result variable, which will hold our final answer. We set it to 1, because we are going to be using it as part of our function later. 
# We then make a for loop, stating for each index in the range of our pow_num, because we want the loop to cycle however many times we are raising our base_num to. In the loop, we set result to equal result times the base_num. Since result starts at 1, the function will multipy the base_num by 1, then set to be equal to the total. The next loop will multiply the base_num by itself, and the final loop will multiply that total by the base_num, etc. 
# We then return the result, and then outside of our functions scope, we print our function, passing in our two parameters.



