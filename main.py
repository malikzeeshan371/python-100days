from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


# creating an empty list
question_bank = []

# looping through the question data and appending it to a new variable
for question in question_data:
    # creating varuables to access the data from the Question class
    question_text = question["question"]
    question_answer = question["correct_answer"]
    # gathering the data 
    new_question = Question(question_text, question_answer)
    # creating a new question from the question data
    question_bank.append(new_question)
# iterating throught the question data and fetching those datas as per our requirement
# print(question_bank[0].text, question_bank[0].answer)
quiz = QuizBrain(question_bank)

quiz.next_question()

while quiz.still_has_questions:
    quiz.next_question()



print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
