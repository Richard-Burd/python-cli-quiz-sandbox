from Objects import Question, Student, Book

# This is a list (Python lists are Ruby arrays) of questions
question_prompts = [
    "Where is Abu Musa Island?\n(a) Persian Gulf\n(b) Arabian Sea\n(c) Gulf of Oman\n\n",
    "Where is Socotra Island?\n(a) Andaman Sea\n(b) Arabian Sea\n(c) Red Sea\n\n",
    "Where is Rhodes Island?\n(a) Lake Baikal\n(b) Tyrrhenian Sea\n(c) Mediterranean Sea\n\n"
]

# This is another list that defines both the question and the correct question answer.
questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "c")
]

# Here are some tests before making the function to run the application:
# print("the question prompt is " + str(questions[0].prompt))
# print("the question answer is " + str(questions[0].answer))

def run_test(questions):
    score = 0
    for question in questions:

        # Retrieve input from the bash command prompt.
        # <<input>> is used for Python v.3:
        # answer = input(question.prompt)
        # ...whereas <<raw_input>> is used for Python v.2
        # ...since I am currently running Python 2.7:
        answer = raw_input(question.prompt)
        if answer == question.answer:
            score += 1
    # "str" converts the score to a string
    # "len" counts the leingth of the questions list
    print("You got " + str(score) + " out of " + str(len(questions)) + " correct\n")

# This method only seems to work when using the PyCharm IDE...this sucks!
# The code doesn't work because the input isn't recognized as a data type
run_test(questions)

student_1 = Student("Thomas", "Architecture",  3.1, False)
war_n_peace = Book("War and Peace", "Leo Tolstoy",  student_1)
print("...and just ecause the other objects are collaborating properly...")
print("A student named %s owns a book entitled %s."%(student_1.name, war_n_peace.title))