# Our Chinese Chef can do everything that our generic Chef can do, but he can also make some fried rice, and he makes an orange chicken special dish.
# In order to allow ChineseChef class to inherit the attributes of our generic Chef, all we have to do is import our Chef class, and then pass Chef as a parameter into our ChineseChef class:
from Chef import Chef

class ChineseChef(Chef):
    
    def make_special_dish(self):
        print("The chef makes you a saucy orange chicken dish")

    def make_fried_rice(self):
        print("The chef makes some DANK fried rice")

# We can then add any additional information, and it will add that on for the ChineseChef only. ALSO, if there are any attributes that get passed in that we would like to override, we can just specify that in this ChineseChef class as well, for example, we want his special dish to be different than the generic Chef special dish, so we make a new function by the same name, and then depending on which chef object we specify when we call the function, it will yield different results.