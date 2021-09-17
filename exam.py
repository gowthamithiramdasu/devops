marks = [] # stores marks obtained by the student

class Student:
    def __init__(self):
        self.li=[['10001','0806'],['10002','2505'],['10003','1504'],['10004','3006'],['10005','0907'],['10006','2512'],['10007','0507']]
       
    # student registration
    def register(self):
        print("--------------------")
        print("STUDENT REGISTRATION")
        print("--------------------")
        self.firstname=input("Enter First Name: ")
        self.lastname=input("Enter Last Name: ")
        self.id=input("Enter Student ID: ")
        self.email=input("Enter Email: ")
        self.password=input("Enter Password: ")
        self.li.append([self.id, self.password]) 
        print("\nRegistration Successful!\n")
    
    # student login
    def login(self):
        print("-------------")
        print("STUDENT LOGIN")
        print("-------------")
        print("\nPlease login to continue...")
        self.id=input("Enter Student ID: ")
        self.password=input("Enter Password: ")
        credentials = [self.id, self.password]
        if credentials in self.li:
            print("Login Successful!\n")
            Student.exams(self, self.firstname)
        else:
            print("Authentication Failed!")
            self.login()
    
    # entering into exam         
    def exams(self, user):
        q1 = QuestionPaper(user, 2345, 20, ['Instruction 1', 'Instruction 2', 'Instruction 3'], 'General Knowledge', 5, '17-September-2021, 9:00 PM', 10, 18, 8)
        q1.display_question_paper()
        q1.agree_instructions()    
        
class QuestionPaper:
        
    def __init__(self, user, id, duration, instructions, subject_name, semester, date_and_time, total_questions, assigned_marks, pass_mark):
        self.user = user
        self.id = id
        self.awarded_marks = []
        self.duration = duration
        self.instructions = instructions
        self.subject_name = subject_name
        self.semester = semester
        self.date_and_time = date_and_time
        self.total_questions = total_questions
        self.assigned_marks = assigned_marks
        self.pass_mark = pass_mark
        
    # display exam details        
    def display_question_paper(self):
        print("-----------------------")
        print("Welcome", self.user)
        print("-----------------------")
        print("\nExam ID:", self.id)
        print("Exam Name:", self.subject_name)
        print("Semester:", self.semester)
        print("Exam Date & Time:", self.date_and_time)
        print("Duration:", self.duration,'minutes')
        print("Number of Questions:", self.total_questions)
        print("Total Assigned Marks:", self.assigned_marks)
        print("Minimum Pass Mark:", self.pass_mark)
        
    # agree exam instructions  
    def agree_instructions(self):
        n=1
        print("\nPlease agree the exam rules to continue.")
        for i in self.instructions:
            print(n,'.',i)
            n = n+1
        print("\nDo you agree? (Type 'Yes' to continue):")
        res =  input()
        res.lower()
        if(res == 'yes'):
            print("\n---------------")
            print("Loading exam...")
            print("---------------\n")
            QuestionPaper.start_test(self)
        else: 
            print("Can't continue without agreeing to the exam rules. Please agree exam rules to continue...")
            self.agree_instructions()
            

    # start the exam    
    def start_test(self):
        mcq1 = MultipleChoiceQuestion(1, 'Capital of India', 1, ['Delhi', 'Mumbai'], 'a')
        mcq2 = MultipleChoiceQuestion(2, 'Capital of Kerala', 1, ['Trivandrum', 'Kochi'], 'a')
        mcq3 = MultipleChoiceQuestion(3, 'Days in a week', 1, ['7', '6'], 'a')
        mcq4 = MultipleChoiceQuestion(4, 'Days in a leap year', 1, ['365', '366'], 'b')
        fib1 = FillInTheBlank(5, '5*10 = ___', 2, '50')
        fib2 = FillInTheBlank(6, 'Biggest planet in solar system is _______ .', 2, 'Jupiter')
        fib3 = FillInTheBlank(7, 'Father of computer ________ .', 2, 'charles babbage')
        fib4 = FillInTheBlank(8, 'C is _____________ programming language.', 2, 'procedural')
        fib5 = FillInTheBlank(9, 'Full form of OS _____________ .', 2, 'operating systems')
        mtf1 = MatchTheFollowing(10, 'Match the following', 4, ['A', 'B', 'C', 'D'], ['E', 'F', 'G', 'H'], ['EFGH', 'FGHE', 'HFGE', 'EHGF'], 'c')
        mcq1.show_question()
        mcq2.show_question()
        mcq3.show_question()
        mcq4.show_question()
        fib1.show_question()
        fib2.show_question()
        fib3.show_question()
        fib4.show_question()
        fib5.show_question()
        mtf1.show_question()
        print("\nSubmitting exam...")
        print("\nGenerating result...")
        QuestionPaper.generate_result(self)
    
    
    # generate exam result    
    def generate_result(self):
        awarded_mark = sum(marks)
        print("-----------")
        print("EXAM RESULT")
        print("-----------")
        print("Name of the Student:", self.user)
        print("Marks Obtained: ", marks)
        print("Total Marks Awarded:", awarded_mark,'/',self.assigned_marks)
        if(awarded_mark >= self.pass_mark):
            print("PASS")
        else:
            print("FAIL")
        if(awarded_mark >= 0.9*self.assigned_marks):
            print("Grade: A")
        elif(awarded_mark >= 0.8*self.assigned_marks < 0.9*self.assigned_marks):
            print("Grade: B")
        elif(awarded_mark >= 0.7*self.assigned_marks < 0.8*self.assigned_marks):
            print("Grade: C")
        elif(awarded_mark >= self.pass_mark < 0.7*self.assigned_marks):
            print("Grade: D")
        else: 
            print("Grade: F")
        
class MultipleChoiceQuestion:
    def __init__(self, qno, qtext, assigned_mark, options, correct_option):
        self.qno = qno
        self.qtext = qtext
        self.assigned_mark = assigned_mark
        self.options = options
        self.correct_option = correct_option
    
    # show MCQ question
    def show_question(self):
        alphabets = ['a', 'b', 'c', 'd']
        print(self.qno,'.',self.qtext,'( Mark:',self.assigned_mark,')')
        for i in range(len(self.options)):
                print(alphabets[i],')', self.options[i])
        response = input("Enter correct option: ")
        MultipleChoiceQuestion.check_answer(self, self.correct_option, response, self.assigned_mark)
    
    # check MCQ answer    
    def check_answer(self, option, response, assigned_mark):
        if(option is response):
            awarded_mark = assigned_mark
            marks.append(awarded_mark)
        else:
            awarded_mark = 0
            marks.append(awarded_mark)
            
            
class FillInTheBlank:
    def __init__(self, qno, qtext, assigned_mark, answer):
        self.qno = qno
        self.qtext = qtext
        self.assigned_mark = assigned_mark
        self.answer = answer
    
    # show Fill In The Blank question
    def show_question(self):    
        print(self.qno,'.',self.qtext,'( Mark:',self.assigned_mark,')')
        res = input("Enter your response: ")
        FillInTheBlank.check_answer(self, self.answer.lower(), res.lower(), self.assigned_mark)
    
    # check fill in the blank answer    
    def check_answer(self, answer, res, assigned_mark):
        if(answer == res):
            awarded_mark = assigned_mark
            marks.append(awarded_mark)
        else:
            awarded_mark = 0
            marks.append(awarded_mark)

 

class MatchTheFollowing:
    def __init__(self, qno, qtext, assigned_mark, question_set, possible_answer_set, correct_answer_set, correct_option):
        self.qno = qno
        self.qtext = qtext
        self.assigned_mark = assigned_mark
        self.question_set = question_set
        self.possible_answer_set = possible_answer_set
        self.correct_answer_set = correct_answer_set
        self.correct_option = correct_option
    
    # show Match the Following question
    def show_question(self):
        alphabets = ['a', 'b', 'c', 'd']
        print(self.qno,'.',self.qtext,'( Mark:',self.assigned_mark,')')
        print("Question Set: ",self.question_set)
        print("Answer Set:   ",self.possible_answer_set)
        for i in range(len(self.correct_answer_set)):
                print(alphabets[i],')', self.correct_answer_set[i])
        response = input("Enter correct option: ")
        MatchTheFollowing.check_answer(self, self.correct_option, response, self.assigned_mark)
    
    # check match the following answer    
    def check_answer(self, option, response, assigned_mark):
        if(option is response):
            awarded_mark = assigned_mark
            marks.append(awarded_mark)
        else:
            awarded_mark = 0
            marks.append(awarded_mark)

 

x=Student()
x.register()
x.login()

