class QuizBrain:
    def __init__(self,  questions_list) -> None:
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.questions_list)

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(
            f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question)

    def check_answer(self, user_answer, current_question):
        if user_answer.lower() == current_question.answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong")
        print(f"The correct answer was: {current_question.answer}")
        print(f"Your current score is: {self.score}/{self.question_number}\n")

    def show_final_score(self):
        print("You completed the quiz")
        print(f"Your final score was: {self.score}/{self.question_number}")