from Questions import Questions

question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Black (Like my soul)\n(c) Orange\n\n",
    "What color are bananas?\n(a) Green\n(b) Pink\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

questions = [
    Questions(question_prompts[0], "a"),
    Questions(question_prompts[1], "c"),
    Questions(question_prompts[2], "b")
]






def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            print("CORRECT!")
            score += 1
        else:
            print("INCORRECT YA NOOB")
    print("You got " + str(score) + "/" + str(len(questions)) + " correct.")

run_test(questions)