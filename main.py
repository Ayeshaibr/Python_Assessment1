from tkinter import *
import random
from PIL import Image, ImageTk

names_list = []
asked = []


def randomiser():
    global qnum
    qnum = random.randint(1,10)
    if qnum not in asked:
      asked.append(qnum)
    elif qnum in asked:
      randomiser()


class StartingPage:
  def __init__(self, parent):
    background_color = "OldLace"
    
    
    self.entry_box= Entry (parent)
    self.entry_box.place(width=200,height=28,x=150,y=390)

    self.continue_button = Button (parent, text = "Start", bg= "pink", command=self.name_collection)
    self.continue_button.place(width=100,height=35,x=200, y=440)
    
  def name_collection(self):
    name = self.entry_box.get()
    names_list.append(name)
    self.entry_box.destroy()
    self.continue_button.destroy()
    QuizPage(root) 

class QuizPage:
  def __init__(self, parent):
    background_color = "#0F044C"
    self.quiz_frame = Frame (parent, bg = background_color, padx = 30, pady = 30)
    self.quiz_frame.grid()
    
    randomiser()

    self.question_label = Label (self.quiz_frame, text = questions_answers[qnum][0], font=("Tw Cen MT", "17", "bold"), bg="grey", highlightthickness=4, highlightcolor= "white")
    self.question_label.grid(row=0, column=0)

    self.var1 = IntVar()
    

    #radio button 1 to hold first choice answer
    self.rb1 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][1], font=("Helvetica", "12"), bg=background_color, fg="white", value=1, padx=10, pady=10, variable=self.var1, background=background_color)
    self.rb1.grid(row=1,pady=9, sticky=W)

    #radio button 2
    self.rb2 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][2], font=("Helvetica", "12"), bg=background_color, value=2, fg="white", selectcolor= "white", padx=10, pady=10, variable=self.var1, background=background_color)
    self.rb2.grid(row=2, pady=5, sticky=W)

    #radio button 3
    self.rb3 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][3], font=("Helvetica", "12"), bg=background_color, value=3,fg="white", padx=10, pady=10,
                            variable=self.var1, background=background_color)
    self.rb3.grid(row=3, pady=5, sticky=W)

    #radio button 4
    self.rb4 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][4], font=("Helvetica", "12"), bg=background_color, value=4, fg="white", padx=10, pady=10, 
                            variable=self.var1, background=background_color)
    self.rb4.grid(row=4, pady=5, sticky=W)

    #confirm answer button 
    self.confirm_button = Button (self.quiz_frame, text = "Confirm", bg="light blue", command=self.test_progress)
    self.confirm_button.grid(row=5, pady=10)

    #score label to show score (test result so far)
    self.score_label=Label(self.quiz_frame, text="SCORE", font=("TW Cen MT","16"), bg=background_color,)
    self.score_label.grid(row=6, pady=1)
    
    

  #Method for Editing the question label and radio buttons to show the next questions data
  def questions_setup(self):
    randomiser()
    self.var1.set(0)
    self.question_label.config(text=questions_answers[qnum][0], )
    self.rb1.config(text=questions_answers[qnum][1])
    self.rb2.config(text=questions_answers[qnum][2])
    self.rb3.config(text=questions_answers[qnum][3])
    self.rb4.config(text=questions_answers[qnum][4])

  #this is the method that would get invoked when confirm answer button is cicked, to take care of progress 
  def test_progress(self):
    global score 
    score=0
    scr_label = self.score_label
    choice = self.var1.get()
    if len(asked)>9: #if question is last
      if choice == questions_answers[qnum][6]: #if last question answer is correct
        score +=1
        scr_label.configure(text=score)
        self.confirm_button.config(text="Confirm")
      else: #if last question answer is wrong
        score +=0
        scr_label.configure(text="The correct answer is " + questions_answers[qnum][5])
        self.confirm_button.config(text="Confirm")
    else: #if not the last question
      if choice==0: #if user has not made a choice
        self.confirm_button.config(text="Try again please, you didn't select anything")
        choice=self.var1.get()
      else: #if user made a choice AND it is NOT the last question
        if choice==questions_answers[qnum][6]: #if choice is correct
          score +=1
          scr_label.configure(text=score)
          self.confirm_button.config(text="Confirm")
          self.questions_setup() #run this method to move to next question
        else: #if choice is wrong
          score +=0
          scr_label.configure(text="The correct answer is " + questions_answers[qnum][5])
          self.confirm_button.config(text="Confirm")
          self.questions_setup()
          


      
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
    
  questions_answers = {
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