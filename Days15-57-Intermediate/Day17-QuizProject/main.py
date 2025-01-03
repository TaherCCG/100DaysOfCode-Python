from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Initialise an empty list to hold question objects
question_bank = []

# Iterate through each question in the question_data
for question in question_data:
    question_text = question["text"]  
    question_answer = question["answer"] 
    new_question = Question(question_text, question_answer) 
    question_bank.append(new_question)  
    
# Create a QuizBrain object with the question_bank
quiz = QuizBrain(question_bank)

# Continue asking questions while there are still questions remaining
while quiz.still_has_questions():
    quiz.next_question()
    
# Print the quiz completion message and final score
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
