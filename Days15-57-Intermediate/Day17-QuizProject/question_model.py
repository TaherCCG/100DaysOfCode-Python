class Question:
    """
    A class to represent a quiz question.

    Attributes:
    text (str): The text of the question.
    answer (str): The correct answer to the question.
    """
    
    def __init__(self, text, answer):
        """
        Initialise the Question object.

        Parameters:
        text (str): The text of the question.
        answer (str): The correct answer to the question.
        """
        self.text = text
        self.answer = answer
