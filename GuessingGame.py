secret_word = "Python"
guess = ""
guess_count = 0
guess_limit = 5
out_of_guesses = False
remaining_guesses = 5

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        print(remaining_guesses)
        guess = input("Enter guess: ")
        guess_count += 1
        remaining_guesses -= 1
        print("Try Again!")

    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of guesses, YOU LOSE MAN")
else:
    print("YO YO YO YOU GOT IT OMG")
