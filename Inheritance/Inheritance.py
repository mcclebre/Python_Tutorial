# Inheritance allows us to define attributes for one class, and then we can define another class and have it inherit all of the attributes from the other class, without having to manually rewrite a bunch of the same information.

# Below I have just the generic chef, and this works the same way as what we did in the Classes&Objects folder.
from Chef import Chef

myChef = Chef() # Creates chef object
myChef.make_chicken() # The chef makes some chicken. Dank.

# Now lets say we want to create a class that models a Chinese Chef...
# (Check out ChineseChef.py for the creation of this class, and how we can make it inherit attributes from our generic Chef.)

from ChineseChef import ChineseChef

myChineseChef = ChineseChef()
myChineseChef.make_salad()
myChineseChef.make_special_dish()

# Now, because we let our ChineseChef class inherit from our Chef class, we can run any functions that we could run with our Chef class, and get those results (or new results if we override them like we did with make_special_dish), and we can also run our new fried rice function!