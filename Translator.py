# Flimish Language
# Any vowels become "Flim"
#---------------------------

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "Flim"
            translation = translation + "flim"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))