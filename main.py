from tkinter import *
import random
from PIL import Image, ImageTk

names_list = []
global questions_answers
asked = []

questions_answers = {
  1: ["What must you do when you see blue and red flashing lights behind you?", 'Speed up to get out of the way', 'Slow down and drive carefully', 'Slow down and stop', 'Drive on as usual', 'Slow down and stop', 3],
  2: ["You may stop on a motorway only:", 'If there is an emergency', 'To let down or pick up passengers', 'To make a U-turn', 'To stop and take a photo', 'If there is an emergency', 1],
  3: ["When coming up to a pedestrian crossing without a raised traffic island, what must you do?", 'Speed up before the pedestrians cross', 'Stop and give way to pedestrians on any part of the crossing', 'Sound the horn on your vehicle to warn the pedestrians', 'Slow down to 30km/h', 'Stop and give way to pedestrians on any part of the crossing', 2],
  4: ["Can you stop on a bus stop in a private motor vehicle?", 'Only between midnight and 6am', 'Under no circumstances', 'When dropping off passengers', 'Only if it is less than 5 minutes', 'Under no circumstances', 2],
  5: ["What is the maximum speed you may drive if you have a 'space saver wheel' fitted? (km/h)", '70 km/h', '100 km/h so you do not hold up traffic', '80 km/h and if the wheel spacer displays a lower limit that applies', '90 km/h', '80 km/h and if the wheel spacer displays a lower limit that applies', 3],
  6: ["When following another vehicle on a dusty road, you should:", 'Speed up to get passed', "Turn your vehicle's windscreen wipers on", 'Stay back from the dust cloud', "Turn you vehicle's headlights on", 'Stay back from the dust cloud', 3],
  7: ["What does the sign containing the letters 'LSZ' mean", "Low safety zone", "Low stability zone", "Lone star zone", "Limited speed zone", "Limited speed zone", 4],
  8: ["What speed are you allowed to pass a school bus that has stopped to let students get on or off?", '20 km/h', '30 km/h', '70 km/h', '10 km/h', '20 km/h', 1],
  9: ["What is the maximum distance a load may extend in front of a car?", '2 meters forward of the front edge of the front seat', '4 meters forward of the front edge of the front seat', '3 meters forward of the front edge of the front seat', '2.5 meters forward of the front edge of the front seat', '3 meters forward of the front edge of the front seat', 3],
  10: ["To avoid being blinded by the headlights of another vehicle coming towards you, what should you do?", 'Look to the left of the road', 'Look to the centre of the road', 'Wear sunglsses that have sufficient strength', 'Look to the right side of the road', 'Look to the left of the road', 1]

}

def randomiser():
    global qnum
    qnum = random.randint(1,10)
    if qnum not in asked:
      asked.append(qnum)
    elif qnum in asked:
      randomiser()




class QuizStarter:
  def __init__(self, parent):
    background_color = "OldLace"
    
    self.heading_label = Label (parent, text = "Sleep Quiz", font=("Tw Cen MT", "18", "bold"), bg=background_color)
    self.heading_label.place(x=10,y=200)
    
    self.user_label = Label (parent, text = "Please enter your name below", font=("Tw Cen MT", "16"), bg=background_color)
    self.user_label.grid(row=1, pady=20)

    self.entry_box= Entry (parent)
    self.entry_box.grid(row=2, pady=20 )

    self.continue_button = Button (parent, text = "Continue", bg= "pink", command=self.name_collection)
    self.continue_button.grid(row=3, pady=20)
    
  def name_collection(self):
    name = self.entry_box.get()
    names_list.append(name)
    print(names_list)
    self.quiz_frame.destroy()
    Quiz(root) 

class Quiz:
  def __init__(self, parent):
    background_color = "OldLace"
    self.quiz_frame = Frame (parent, bg = background_color, padx = 100, pady = 100)
    self.quiz_frame.grid()
    
    randomiser()

    self.question_label = Label (self.quiz_frame, text = questions_answers[qnum][0], font=("Tw Cen MT", "18", "bold"), bg=background_color)
    self.question_label.grid(row=0, padx=10, pady=10)

    self.var1 = IntVar()
    

    #radio button 1 to hold first choice answer
    self.rb1 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][1], font=("Helvetica", "12"), bg=background_color, value=1, padx=10, pady=10,
                           variable=self.var1, background=background_color)
    self.rb1.grid(row=1, sticky=W)

    #radio button 2
    self.rb2 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][2], font=("Helvetica", "12"), bg=background_color, value=2, padx=10, pady=10, 
                           variable=self.var1, background=background_color)
    self.rb2.grid(row=2, sticky=W)

    #radio button 3
    self.rb3 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][3], font=("Helvetica", "12"), bg=background_color, value=3, padx=10, pady=10,
                            variable=self.var1, background=background_color)
    self.rb3.grid(row=3, sticky=W)

    #radio button 4
    self.rb4 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][4], font=("Helvetica", "12"), bg=background_color, value=4, padx=10, pady=10,
                            variable=self.var1, background=background_color)
    self.rb4.grid(row=4, sticky=W)

    #confirm answer button 
    self.confirm_button = Button (self.quiz_frame, text = "Confirm", bg="light blue", command=self.test_progress)
    self.confirm_button.grid(row=5)

    #score label to show score (test result so far)
    self.score_label=Label(self.quiz_frame, text="SCORE", font=("TW Cen MT","16"), bg=background_color,)
    self.score_label.grid(row=6, pady=1)
    
    

  #Method for Editing the question label and radio buttons to show the next questions data
  def questions_setup(self):
    randomiser()
    self.var1.set(0)
    self.question_label.config(text=questions_answers[qnum][0])
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
  quizStarter_object = QuizStarter(root)
  root.mainloop()