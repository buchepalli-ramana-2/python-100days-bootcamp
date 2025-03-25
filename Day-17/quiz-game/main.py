from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    newquestion = Question(question_text, question_answer)
    question_bank.append(newquestion)

# print(question_bank[0].text,question_bank[0].answer)
quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.nextquestion()

print(f"You have been completed the Quiz!!")
print(f"Your score was {quiz.score}/{quiz.question_number}")

