import data
import question_model
import quiz_brain

question_list = []
for question in data.question_data:
    text = question["question"]
    answer = question["correct_answer"]
    new_question = question_model.Questions(text, answer)
    question_list.append(new_question)

game = quiz_brain.QuizGame(question_list)

while game.still_has_questions():
    game.ask_question()

print("You have completed the quiz!")
print(f"Your final score is {game.score}")