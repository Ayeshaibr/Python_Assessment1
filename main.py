from tkinter import *
import random
from PIL import Image, ImageTk
from tkinter import messagebox


names_list = []
asked = []
score = 0 


def randomize():
    global qnumber
    qnumber = random.randint(1,10)
    if qnumber not in asked:
      asked.append(qnumber)
    elif qnumber in asked:
      randomize()


class StartingPage:
  def __init__(self, parent):
    background_color = "OldLace"
    
    
    self.entry_box= Entry (parent)
    self.entry_box.place(width=200,height=28,x=150,y=390)

    self.continue_button = Button (parent, text = "Start", bg= "pink", command=self.username_check)
    self.continue_button.place(width=100,height=35,x=200, y=440)

  def username_check(self):
        name = self.entry_box.get()
        if name == '' or len(name) >= 9:
            messagebox.showerror(message='Please enter a username between 1 and 9 characters!')  # shows error message
        else:
            self.name_collection()
          
  def name_collection(self):
    name = self.entry_box.get()
    names_list.append(name)
      
    self.entry_box.destroy()
    self.continue_button.destroy()
    QuizPage(root) 

class QuizPage:
  def __init__(self, parent):
    background_color = "#0F044C"
    self.quiz_frame = Frame (parent, bg = background_color, padx = 25, pady = 30)
    self.quiz_frame.grid()
    
    randomize()

    self.question_label = Label (self.quiz_frame, text = quiz_content[qnumber][0], font=("Tw Cen MT", "17", "bold"), bg="grey", highlightthickness=4, highlightcolor= "white")
    self.question_label.grid(row=0, column=0, sticky=W)

    self.var1 = IntVar()
    

    #radio button 1 to hold first choice answer
    self.rb1 = Radiobutton (self.quiz_frame, text = quiz_content[qnumber][1], font=("Helvetica", "12"), bg=background_color, fg="white", value=1, padx=10, pady=10, variable=self.var1, selectcolor= "#0F044C", background=background_color)
    self.rb1.grid(row=1,pady=9, sticky=W)

    #radio button 2
    self.rb2 = Radiobutton (self.quiz_frame, text = quiz_content[qnumber][2], font=("Helvetica", "12"), bg=background_color, value=2, fg="white", selectcolor= "#0F044C", padx=10, pady=10, variable=self.var1, background=background_color)
    self.rb2.grid(row=2, pady=5, sticky=W)

    #radio button 3
    self.rb3 = Radiobutton (self.quiz_frame, text = quiz_content[qnumber][3], font=("Helvetica", "12"), bg=background_color, selectcolor= "#0F044C", value=3,fg="white", padx=10, pady=10,
                            variable=self.var1, background=background_color)
    self.rb3.grid(row=3, pady=5, sticky=W)

    #radio button 4
    self.rb4 = Radiobutton (self.quiz_frame, text = quiz_content[qnumber][4], font=("Helvetica", "12"), bg=background_color, selectcolor= "#0F044C", value=4, fg="white", padx=10, pady=10, 
                            variable=self.var1, background=background_color)
    self.rb4.grid(row=4, pady=5, sticky=W)

    #confirm answer button 
    self.confirm_button = Button (self.quiz_frame, text = "Confirm", bg="white", command=self.score_progress)
    self.confirm_button.grid(row=6, pady=10, sticky=E)

    #score label to show score (test result so far)
    self.score_label=Label(self.quiz_frame, text="SCORE", font=("TW Cen MT","16"), bg=background_color,fg="white")
    self.score_label.grid(row=5, pady=10)

    self.quit_button = Button (self.quiz_frame, text = "Quit", bg="white", command=self.endScreen)
    self.quit_button.grid(row=6, column=0, pady=10,sticky=W)
    
    

  #Method for Editing the question label and radio buttons to show the next questions data
  def questions_layout(self):
    randomize()
    self.var1.set(0)
    self.question_label.config(text=quiz_content[qnumber][0], )
    self.rb1.config(text=quiz_content[qnumber][1])
    self.rb2.config(text=quiz_content[qnumber][2])
    self.rb3.config(text=quiz_content[qnumber][3])
    self.rb4.config(text=quiz_content[qnumber][4])

  #this is the method that would get invoked when confirm answer button is cicked, to take care of progress 
  def score_progress(self): 
        global score # this score needs to be accessible to all questions
        scr_label = self.score_label # renaming the score label each time the score is different
        choice = self.var1.get()
        if len(asked) > 9:  # if question is last
            if choice == quiz_content[qnumber][6]:  # if last question answer is correct
                score += 1
                scr_label.configure(text=score)
                self.endScreen()
            else:

            # if last question answer is wrong

                score += 0
                scr_label.configure(text='The correct answer is '
                                    + quiz_content[qnumber][5])
                self.endScreen()
        else:

          # if not the last question

            if choice == 0:  # if user has not made a choice
                self.confirm_button.config(text="Try again please, you didn't select anything"
                        )
                choice = self.var1.get()
            else:

            # if user made a choice AND it is NOT the last question

                if choice == quiz_content[qnumber][6]:  # if choice is correct
                    score += 1
                    scr_label.configure(text=score)
                    self.confirm_button.config(text='Confirm')
                    self.questions_layout()  # run this method to move to next question
                else:

              # if choice is wrong

                    score += 0
                    scr_label.configure(text='The correct answer is '
                            + quiz_content[qnumber][5])
                    self.confirm_button.config(text='Confirm')
                    self.questions_layout()



  def endScreen(self):
        self.quiz_frame.destroy()
        self.question_label.destroy()
        self.rb1.destroy()
        self.rb2.destroy()
        self.rb3.destroy()
        self.rb4.destroy()
        self.confirm_button.destroy()
        self.score_label.destroy()
        self.quit_button.destroy()
       

    
        name = names_list[0]
        file = open('scoreBoard.txt', 'a')  # opens the highscores file
        if name == 'reset':
            file = open('scoreBoard.txt', 'w')
        else:
            file.write(str(score))  # turns the score into a string
            file.write(' - ')  # writes into the text file
            file.write(name + '\n')  # writes the name into the text file and then goes to a new line
            file.close()  # closes the file
        inputFile = open('scoreBoard.txt', 'r')  # opens the highscores file in read mode
        lineList = inputFile.readlines()  # line list equals the each line in the list
        lineList.sort()
        top = []
        top5 = lineList[-5:]
        for line in top5:
            point = line.split(' - ')
            top.append((int(point[0]), point[1]))
        file.close()
        top.sort()
        top.reverse()
        return_string = ''
        for i in range(len(top)):
            return_string += '{} - {}\n'.format(top[i][0], top[i][1])

        open_endscrn = EndingPage(root)
        open_endscrn.scores_list.config(text=return_string)

class EndingPage:
  def __init__ (self, parent):
    background_color = "#0F044C"
    self.quiz_frame = Frame (parent, bg = background_color, padx = 100, pady = 50)
    self.quiz_frame.grid()
    
    #title for ending page
    self.score_title = Label (self.quiz_frame, text ="Scoreboard", font=("Tw Cen MT", "17", "bold"), bg="grey", highlightthickness=4, highlightcolor= "white")
    self.score_title.grid(row=0, padx=10)
    

    
    self.scores_list = Label (self.quiz_frame, text ="", font=("Tw Cen MT", "17", "bold"), bg="grey", padx=70, pady=10)
    self.scores_list.grid(row=1, pady=10)
    
    #button to go back to first page 
    self.home_button = Button (self.quiz_frame, text = "Home Page", bg="white", command=self.home)
    self.home_button.grid(row=2,  pady=10, sticky=W)


    #quit Button
    self.quit_button = Button (self.quiz_frame, text = "Quit", bg="white", command=self.quit_quiz)
    self.quit_button.grid(row=2,  pady=10, sticky= E)


    
  def quit_quiz(self):
      self.quiz_frame.destroy()
      self.score_title.destroy()
      self.home_button.destroy()
      self.scores_list.destroy()
      self.quit_button.destroy()
      root.withdraw()

  # for the user to restart the quiz
  def home(self):
      self.quiz_frame.destroy()
      self.score_title.destroy()
      self.home_button.destroy()
      self.scores_list.destroy()
      self.quit_button.destroy()
      asked.clear() # clears the asked question list 
      names_list.clear() # clears the name list
      global score, name
      score = 0 # resets the score back to 0 for another attempt
      name = '' 

      StartingPage(root) # opens the home screen

    

    
    

      
#..........Starting point of Program..........#
if __name__ == "__main__":
  root = Tk()
  root.title("Sleep Quiz")
  root.geometry("500x500")

  bg_image = Image.open("sleepquiz.png") #need to use Image if need to resize 
  bg_image = bg_image.resize((500, 500), Image.ANTIALIAS)
  bg_image = ImageTk.PhotoImage(bg_image) 
        #self.bg_image = PhotoImage(file="Sleepquiz.png")

  #label for image
  image_label= Label(root, image=bg_image)
  image_label.place(x=0, y=0, relwidth=1, relheight=1) 
  # make label l to fit the parent window always
    
  quiz_content = {
    1: ["How many hours of sleep do\n teenagers (aged 13-18) need per \n24 hours?", '4-6 hours', '6-8 hours', '8-10 hours', '10-12 hours', '8-10 hours', 3],
    2: ["What is Somnambulism?", "Sleep Walking","Insomnia","Sleep Paralysis","Sleep Apnea","Sleep Walking", 1],
    3: ["Which of the following is the most\n common cause of nightmares?", "Stress and Anxiety", "Eating too much spicy food", "DNA cell mutations", "Excess Dopamine", "Stress and Anxiety", 1 ],
    4: ["Sleep Paralysis\n is the temporary … while falling\n asleep or upon waking.", "Loss of sight", "Pain in the abdomen", "Inability to move or speak", "Blurred vision", "Inability to move or speak", 3],
    5: ["What are the effects of Sleep\n Deprivation or poor sleeping\n habits?", "Memory issues and trouble with concentration", "Increased risk of Diabetes and Heart Disease", "Weakened immune system and Weight Gain", "All of the above", "All of the above",4],
    6: ["Which mammals willingly delay\n their sleep?", "Whales", "Humans", "Monkeys", "All of the above","Humans",2],
    7: ["Sleep apnea is identified by pauses\nin breathing while you\nsleep, which can occur how many\ntimes per hour?", "Upto 5 times", "Upto 10 times", "Upto 20 times", "30 times or more", "30 times or more", 4 ],
    8: ["Which animals hold each others’\n hands when they sleep?", "Wolves", "Sea Otters", "Red Pandas", "Lions", "Sea Otters", 2 ],
    9: ["What is the normal time it takes\n for most people to fall asleep\n at night?", "5-10 minutes", "10-20 minutes", "20-30 minutes", "30-40 minutes", "10-20 minutes", 2],
    10: ["In which phase during sleep is the\n brain the most active, and has\n the most  vivid dreams?", "REM", "Post-Drome", "Retinopathy", "Metaphase", "REM", 1]
  
  }
  quizStarter_object = StartingPage(root)
  root.mainloop()