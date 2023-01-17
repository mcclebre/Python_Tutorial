# You can make two dimensional lists (lists in a list(inception af))
# Remember, lists are just like arrays(JS)
# number_grid = [
#     [1,2,3],
#     [4,5,6],          
#     [7,8,9],        
#     [0]
# ]
# print(number_grid[0][0])

#This number_grid list has 4 elements, which are each lists themselves.
# This example is set up to look like a grid for the ease of understanding how you can access different elements inside of two dimensional lists. When returning/printing the list number_grid, you can specify two index's with [][]. The first [] will be the element of the overall list, in this case the columns of the grid. The second [] will be the element within the list selected by the first [].
#So, number_grid[0][0] would return 1, number_grid[2][1] would return 8, etc...

#///////////////////////NESTED FOR LOOP/////////////////////////////
# number_grid = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
#     [0]
# ]

# for row in number_grid:
#     print(row)

# This prints exactly what we have written in number_grid. If we want to loop through all of the nested list elements inside of number_grid, we can use a nested for loop, like this:

# number_grid = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
#     [0]
# ]

# for row in number_grid:
#     for col in row:
#         print(col)

#This prints 1-9 and 0, because you are looping through each element inside each list inside of number_grid, from top to bottom/ front to back.

