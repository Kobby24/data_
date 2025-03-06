class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.questions_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def next_question(self):
        current_question = self.questions_list[self.question_number]

        user_answer = input(f"Q{self.question_number + 1}.: {current_question.text} (True/False): ")
        self.question_number += 1

        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print(f"You got it right!")

        else:
            print("That's wrong")
        print(f"The correct answer is {correct_answer}")
        print(f"Your Current Score is {self.score}/{self.question_number}")
        print("\n")