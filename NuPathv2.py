import requests
from random import shuffle
import html
from tkinter import Tk, Canvas, StringVar, Label, Radiobutton, Button, messagebox
import math
import os
import sys
import html


BUTTON_WIDTH = 10
THEME_COLOR = "#375362"

class Question:
    def __init__(self, question: str, correct_answer: str, choices: list):
        self.question_text = question
        self.correct_answer = correct_answer
        self.choices = choices

class QuizBrain:

    def __init__(self, questions):
        self.question_no = 0
        self.score = 0
        self.questions = questions
        self.current_question = None

    def has_more_questions(self):
        """To check if the quiz has more questions"""
        
        return self.question_no < len(self.questions)

    def next_question(self):
        """Get the next question by incrementing the question number"""
        
        self.current_question = self.questions[self.question_no]
        self.question_no += 1
        q_text = self.current_question.question_text
        return f"Q.{self.question_no}: {q_text}"

    def check_answer(self, user_answer):
        """Check the user answer against the correct answer and maintain the score"""
        
        correct_answer = self.current_question.correct_answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False

    def get_score(self):
        """Get the number of correct answers, wrong answers and score percentage."""
        
        wrong = self.question_no - self.score
        score_percent = int(self.score / self.question_no * 100)
        return (self.score, wrong, score_percent)

class resultUI():
    def __init__(self):
        self.resultwindow = Tk()
        self.resultwindow.title("Results")
        self.resultwindow.attributes('-fullscreen', True)
        # Title
        self.display_title(self.resultwindow)

        # Creating start buttons
        self.display_results()

        # Mainloop the window
        self.resultwindow.mainloop()
    
    def display_title(self, windowname):
        """To display title"""
        maxwidth = self.resultwindow.winfo_screenwidth() 

        # Title
        title = Label(windowname, text="NuPath",
                      width=math.ceil(maxwidth), bg="gold", fg="white", font=("HP Simplified", 20, "bold"))

        # place of the title
        title.place(relx=0.5, y=0, anchor='n')

    def display_results(self):
        """To display the result using messagebox"""
        correct, wrong, score_percent = self.quiz.get_score()

        correct = f"Correct: {correct}"
        wrong = f"Wrong: {wrong}"

        # calculates the percentage of correct answers
        result = f"Score: {score_percent}%"
        print(result, correct, wrong)

class QuizInterface:

    def __init__(self, quiz_methods: QuizBrain) -> None:
        self.q_ui(quiz_methods)

    def q_ui(self, quiz_methods):
        self.quiz = quiz_methods
        self.quizwindow = Tk()
        self.quizwindow.title("Quiz Application")
        self.quizwindow.attributes('-fullscreen', True)
        self.quizwindow.attributes('-topmost',True)
        maxwidth = self.quizwindow.winfo_screenwidth() 
        maxheight= self.quizwindow.winfo_screenheight()
        

        # Display title
        self.display_title(self.quizwindow)

        # Create a canvas for question text, and dsiplay question
        self.canvas = Canvas(width=maxwidth, height=maxheight)
        self.question_text = self.canvas.create_text(math.floor(maxwidth/2.125), math.floor(maxheight/3.24),
                                                     text="Question here",
                                                     width=math.floor(maxwidth/1.25),
                                                     fill=THEME_COLOR,
                                                     font=(
                                                         'Calibri', 15, 'italic')
                                                     )
        self.canvas.grid(row=2, column=0, columnspan=2, pady=math.floor(maxheight/10.6))
        self.display_question()

        # Declare a StringVar to store user's answer
        self.user_answer = StringVar()

        # Display four options as radio buttons
        self.opts = self.radio_buttons()
        self.display_options()

        # To show whether the answer is right or wrong
        self.feedback = Label(self.quizwindow, pady=10, font=("Calibri", 15, "bold"))
        self.feedback.place(relx=0.5, y=math.floor(maxheight/1.35), anchor='center')

        # Next, home and quit buttons
        self.quizbuttons()

        #   loop
        self.quizwindow.mainloop()
    
    def home_btn(self):
        self.quizwindow.destroy()
        # set up home window
        self.homewindow = Tk()
        self.homewindow.title("Quiz Application")
        self.homewindow.attributes('-fullscreen', True)
        self.homewindow.attributes('-topmost',True)
        # Title
        self.display_title(self.homewindow)
        
        #Creating home screen buttons
        self.homebuttons()
     
    def quiz_scrn(self, quiz_methods: QuizBrain) -> None:
        self.quiz = quiz_methods
        self.quizwindow = Tk()
        self.quizwindow.title("Quiz Application")
        self.quizwindow.attributes('-fullscreen', True)
        self.quizwindow.attributes('-topmost',True)
        maxwidth = self.quizwindow.winfo_screenwidth() 
        maxheight= self.quizwindow.winfo_screenheight()
        

        # Display Title
        self.display_title(self.quizwindow)

        # Create a canvas for question text, and dsiplay question
        self.canvas = Canvas(width=maxwidth, height=maxheight)
        self.question_text = self.canvas.create_text(math.floor(maxwidth/2.125), math.floor(maxheight/4.24),
                                                     text="Question here",
                                                     width=math.floor(maxwidth/1.25),
                                                     fill=THEME_COLOR,
                                                     font=(
                                                         'Calibri', 15, 'italic')
                                                     )
        self.canvas.grid(row=2, column=0, columnspan=2, pady=math.floor(maxheight/10.6))
        self.display_question()
        
        # Declare a StringVar to store user's answer
        self.user_answer = StringVar()

        # Display four options (radio buttons)
        self.opts = self.radio_buttons()
        self.display_options()

        # To show whether the answer is right or wrong
        self.feedback = Label(self.quizwindow, pady=10, font=("Calibri", 15, "bold"))
        self.feedback.place(relx=0.5, y=math.floor(maxheight/1.35), anchor='center')

        # Next and Quit Button
        self.quizbuttons()

        #   loop
        self.quizwindow.mainloop()
    
    def home_btn(self):
        self.quizwindow.destroy()
        # set up home window
        self.homewindow = Tk()
        self.homewindow.title("Quiz Application")
        self.homewindow.attributes('-fullscreen', True)
        self.homewindow.attributes('-topmost',True)
        # Title
        self.display_title(self.homewindow)
        
        #Creating home screen buttons
        self.homebuttons()

    def homebuttons(self):
        """To show quit, info, start buttons"""

        maxwidth = self.homewindow.winfo_screenwidth() 
        maxheight= self.homewindow.winfo_screenheight()

        # This is the second button which is used to quit the self.homewindow
        quit_button = Button(self.homewindow, text="Quit", command=self.homewindow.destroy,
                             width=int(BUTTON_WIDTH/2), bg="red", fg="white", font=("Magneto", 16, "bold"))

        # placing the quit button on the screen
        quit_button.place(x=math.floor(maxwidth/1.1), y=math.floor(maxheight/10.6))
        # creating start button
        start_button = Button(self.homewindow, text="Start", command=self.homewindow, bg="#00ff00", fg = "white", font =("Magneto", 22),
                             width = BUTTON_WIDTH)
        start_button.place(relx = 0.5, rely = 1/3, anchor = 'center')

        info_button = Button(self.homewindow, text="Info", command=self.display_result, bg="blue", fg = "white", font =("Magneto", 22),
                             width = BUTTON_WIDTH)
        info_button.place(relx = 0.5, rely = 2/3, anchor = 'center')
        

    def display_title(self, windowname):
        """To display title"""
        maxwidth = windowname.winfo_screenwidth() 

        # Title
        title = Label(windowname, text="NuPath",
                      width=math.ceil(maxwidth), bg="gold", fg="white", font=("Magneto", 20, "bold"))

        # place of the title
        title.place(relx=0.5, y=0, anchor='n')

    def display_question(self):
        """To display the question"""

        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def radio_buttons(self):
        """To create four options (radio buttons)"""

        maxwidth = self.quizwindow.winfo_screenwidth() 
        maxheight= self.quizwindow.winfo_screenheight()

        # create empty list for choices to be appended to
        choice_list = []

        # position of the first option
        y_pos = math.floor(maxheight/2.41)

        # adding the options to the list
        while len(choice_list) < 4: 

            # setting the radio button properties
            radio_btn = Radiobutton(self.quizwindow, text="", variable=self.user_answer,
                                    value='', font=("Calibri", 14))

            # adding the button to the list
            choice_list.append(radio_btn)

            # placing the button
            radio_btn.place(x=math.ceil(maxwidth/4.25), y=y_pos)

            # incrementing the y-axis position by 40
            y_pos += math.ceil(maxheight/13.25)

        # return the radio buttons
        return choice_list

    def display_options(self):
        """To display four options"""

        val = 0

        # deselecting the options
        self.user_answer.set(None)

        # looping over the options to be displayed for the
        # text of the radio buttons.
        for option in self.quiz.current_question.choices:
            self.opts[val]['text'] = option
            self.opts[val]['value'] = option
            val += 1

    def next_btn(self):
        """To show feedback for each answer and keep checking for more questions"""

        # Check if the answer is correct
        if self.quiz.check_answer(self.user_answer.get()):
            self.feedback["fg"] = "green"
            self.feedback["text"] = 'Answer has been recorded! \U0001F44D'
        

        if self.quiz.has_more_questions():
            # Moves to next to display next question and its options
            self.display_question()
            self.display_options()
        else:
            # if no more questions, then it displays the score
            resultUI(quiz)
            self.replaybutton()

    

    def quizbuttons(self):
        """To show next button and quit button"""

        maxwidth = self.quizwindow.winfo_screenwidth() 
        maxheight= self.quizwindow.winfo_screenheight()
        

        # Next button to move to the next question
        next_button = Button(self.quizwindow, text="Next", command=self.next_btn,
                             width=BUTTON_WIDTH, bg="green", fg="white", font=("Magneto", 16, "bold"))

        # placing the button on the screen
        next_button.place(relx=0.5, y=math.floor(maxheight/1.16), anchor='center')

        # This is the second button which is used to quit the self.quizwindow
        quit_button = Button(self.quizwindow, text="Quit", command=self.quizwindow.destroy,
                             width=int(BUTTON_WIDTH/2), bg="red", fg="white", font=("Magneto", 16, "bold"))

        # placing the Quit button on the screen
        quit_button.place(x=math.floor(maxwidth/1.1), y=math.floor(maxheight/10.6))

        # Third button which takes user back to home screen
        home_button = Button(self.quizwindow, text = "Home", command=self.home_btn,
                             width=int(BUTTON_WIDTH/2), bg="blue", fg="white", font=("Magneto", 16, "bold"))
        
        home_button.place(x=math.floor(maxwidth/1.2), y=math.floor(maxheight/10.6))

    def replaybutton(self):
        """Display replay button when quiz ends"""    
        maxheight= self.quizwindow.winfo_screenheight()

        # Next button to move to the next question
        replay_button = Button(self.quizwindow, text="Replay", command=self.homewindow,
                             width=BUTTON_WIDTH, bg="green", fg="white", font=("Helvetica", 16, "bold"))

        # Placing the button on the screen
        replay_button.place(relx=0.5, y=math.floor(maxheight/1.16), anchor='center')



    def home(self):
        self.userwindow()
        exec(open(os.path.abspath("c:/Users/krish/OneDrive/Desktop/NuPathv2.py")).read()) #Restarts file

    def display_result(self):
        """To display the result using messagebox"""
        correct, wrong, score_percent = self.quiz.get_score()

        correct = f"Correct: {correct}"
        wrong = f"Wrong: {wrong}"

        # calculates the percentage of correct answers
        result = f"Score: {score_percent}%"

        # Shows a message box to give brief info
        messagebox.showinfo("Information on us", f"NuPath is an application aimed to help students from age 16 - 21 decide which career or university oppurtunity fits them the best")

parameters = {
    "amount": 2,
    "type": "multiple"
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
question_data = response.json()["results"]

question_bank = []
for question in question_data:
    choices = []
    question_text = html.unescape(question["question"])
    correct_answer = html.unescape(question["correct_answer"])
    incorrect_answers = question["incorrect_answers"]
    for ans in incorrect_answers:
        choices.append(html.unescape(ans))
    choices.append(correct_answer)
    shuffle(choices)
    new_question = Question(question_text, correct_answer, choices)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

quiz_ui = QuizInterface(quiz)


print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_no}")
