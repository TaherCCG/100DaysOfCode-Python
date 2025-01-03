class QuizBrain:
    """
    A class to represent the quiz game logic.
    
    Attributes:
    question_number (int): The current question number.
    question_list (list): A list of question objects.
    score (int): The current score of the player.
    """
    
    def __init__(self, question_list):
        """
        Initialise the quiz with a list of questions.
        
        Parameters:
        question_list (list): A list of question objects.
        """
        self.question_number = 0
        self.question_list = question_list
        self.score = 0


    def still_has_questions(self):
        """
        Check if there are more questions left in the quiz.
        
        Returns:
        bool: True if there are more questions, False otherwise.
        """
        return self.question_number < len(self.question_list)


    def next_question(self):
        """
        Present the next question to the user and get their answer.
        """
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)


    def check_answer(self, user_answer, correct_answer):
        """
        Check the user's answer against the correct answer and update the score.
        
        Parameters:
        user_answer (str): The user's answer.
        correct_answer (str): The correct answer.
        """
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}\n")
