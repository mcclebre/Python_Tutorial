# A Dictionary in Python is a structure that allows you to store information in "Key Value Pairs". This allows you to store information in different key value pairs into the dictionary, and then when you want to use it later, you can refer to it by its "Key".
# Whenever you are creating a dictionary, you need to put it in {}.
# This is similar to creating an object with JS.

# monthConversions = {
#     "Jan": "January",
#     "Feb": "February",
#     "Mar": "March",
#     "Apr": "April",
#     "May": "May",
#     "Jun": "June",
#     "Jul": "July",
#     "Aug": "August",
#     "Sep": "September",
#     "Nov": "November",
#     "Dec": "December"
# }

# You can now access these values by refering to the dictionary by name, and then using either ["key"], .get("key", "Default Value") (with .get, you can set a default value that will return if the "key" is not found in the dictionary.)

# monthConversions = {
#     "Jan": "January",
#     "Feb": "February",
#     "Mar": "March",
#     "Apr": "April",
#     "May": "May",
#     "Jun": "June",
#     "Jul": "July",
#     "Aug": "August",
#     "Sep": "September",
#     "Nov": "November",
#     "Dec": "December"
# }

# print(monthConversions["Jan"])
# print(monthConversions.get("Sky", "Not a valid Key"))

# You can also set the key as a number, rather than a string.
# monthConversions = {
#     1: "January",
#     2: "February",
#     3: "March",
#     4: "April",
#     5: "May",
#     6: "June",
#     7: "July",
#     8: "August",
#     9: "September",
#     10: "October",
#     11: "November",
#     12: "December"
# }

# print(monthConversions[5])
# print(monthConversions.get(14, "Not a valid Key"))