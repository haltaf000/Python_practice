from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    question_bank.append(Question(question_text, question_answer))


quiz = QuizBrain(question_bank)

while quiz.still_has_quesitons():
    quiz.next_question()

print("You've complete the quiz")
print(f"Your final score was: {quiz.score}/{len(question_bank)} ")