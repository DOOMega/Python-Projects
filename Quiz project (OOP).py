class Question:

    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def check_answer(self, get_answer):
        return self.answer == get_answer

class Quiz:

    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.question_index = 0

    def get_question(self):
        return self.questions[self.question_index]
        
    def display_question(self):
        question = self.get_question()
        print(f'Soru {self.question_index + 1}: {question.text}')
    
        for q in question.choices:
            print('-' + q)

        answer = input("answer:")
        self.guess(answer)
        self.loadquestion()
        

    def guess(self, answer):
        question = self.get_question()

        if question.check_answer(answer):
            self.score +=1
        self.question_index +=1

    def loadquestion(self):
        if len(self.questions) == self.question_index:
            self.show_score()
 
        else:
            self.display_progress()
            self.display_question() 

    def show_score(self):
        print(f"score: {self.score}")
        
    def display_progress(self): 
        total_question = len(self.questions)
        question_number = self.question_index + 1

        if question_number > total_question:
            print('Quiz is over.')
        else:
            print(f' {question_number} of {total_question}'.center(100, '*'))

    
q1 = Question("en iyi programlama dili hangisidir?", ["C#", "python", "javascript", "java"], "python")
q2 = Question("en popüler programlama dili hangisidir?", ["C#", "python", "javascript", "java"], "python")
q3 = Question("en çok kazandıran programlama dili hangisidir?", ["C#", "python", "javascript", "java"], "python")
q4 = Question("en çok sevilen programlama dili hangisidir?", ["C#", "python", "javascript", "java"], "python")
q5 = Question("en kolay programlama dili hangisidir?", ["C#", "python", "javascript", "java"], "python")

questions = [q1,q2,q3,q4,q5]

quiz = Quiz(questions) 

quiz.loadquestion()
