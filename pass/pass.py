class Question:
    def __init__(self, question_text, answer_list):
        self.question_text = question_text
        self.answer_list = answer_list
        self.correct_answer = None
    def add_question(question_text, answer_list):
    new_question = Question(question_text, answer_list)
    questions.append(new_question)
    def remove_question(question_text):
    for question in questions:
        if question.question_text == question_text:
            questions.remove(question)
            return True
    return False
    def edit_question_text(question, new_text):
    question.question_text = new_text

    def edit_answers(question, new_answers):
    question.answer_list = new_answers
    def get_random_question():
    random_index = random.randint(0, len(questions) - 1)
    return questions[]










  
