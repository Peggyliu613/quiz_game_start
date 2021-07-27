class QuizGame:

    def __init__(self,  question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def ask_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        player_answer = input(f"Q{self.question_number}: , {question.text} (T/F): ")
        self.check_answer(player_answer, question.answer)

    def check_answer(self, player_answer, answer):
        if (player_answer.lower() == "t" and answer == "True") or (player_answer.lower() == "f" and answer == "False"):
            print("You got it right!")
            self.score += 1
        else:
            print("Sorry you are wrong.")
        print("The correct answer is", answer)
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
