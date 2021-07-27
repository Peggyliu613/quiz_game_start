import data
import question_model
import quiz_brain

question_list = []
for question in data.question_data:
    text = question["text"]
    answer = question["answer"]
    new_question = question_model.Questions(text, answer)
    question_list.append(new_question)

quiz = quiz_brain.QuizGame(question_list)

while quiz.still_has_questions():
    quiz.ask_question()
