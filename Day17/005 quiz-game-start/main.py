from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

q_bank = []
for question in question_data:
    q_text = question["question"]
    q_answer = question["correct_answer"]
    new_question = Question(q_text, q_answer)
    q_bank.append(new_question)
quiz = QuizBrain(q_bank)
quiz.next_question()

while quiz.still_has_questions():
    quiz.next_question()
print(f"Your Final score is {quiz.score} out of {quiz.question_number} questions")


