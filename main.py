import random
from tkinter import*
from random import choice,shuffle,randint
import pandas
from _testcapi import _test_structmembersType_OldAPI
from pandas import*
BACKGROUND_COLOR= "#B1DDC6"
to_learn={}
try:
    pd = pandas.read_csv("data/words_to_learn.csv") #we have created a dataframe here
except FileNotFoundError:
    original_data=pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient='records')



#now we will create a dict of dataframe
#dict will be haphazard and not to our liking
#we will use the keyword orient to arrange our dict
#by using keyword 'records' it will give us each column-->value
else:
    to_learn=pd.to_dict(orient='records') #we will have list of dictionaries
#print(to_learn) #dict will be haphazard and not to our liking
#now we will pick random enteries from the list and display it
current_card={}
def next_card(): #going to access words in csv file and get hold of french words and their definitions
    global current_card,flip_timer #this will create all the functions of current card on a global scale
    current_card=random.choice(to_learn)
    #print(current_card["French"]) #this is going to pick out random french words for me
    #now instead of printing it on screen we want to put it in canvas
    canvas.itemconfig(card_title,text="french",fill="black")#this will config titile to french
    canvas.itemconfig(card_word,text=current_card["French"],fill="black")
    canvas.itemconfig(canvas_image, image=card_front)
    flip_timer=window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title,text="English",fill="white")
    canvas.itemconfig(card_word, text=current_card["English"],fill="white")
    canvas.itemconfig(canvas_image, image=new_image)

def save_info():
    to_learn.remove(current_card)
    print(len(to_learn))
    data=pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv",index=False) #index is used to not create added columns each time we run our code and words get added into the file
    next_card()



window= Tk()
window.title("Flashcard")
window.config(padx= 50,pady=50,bg=BACKGROUND_COLOR)
flip_timer=window.after(3000,func=flip_card)


canvas=Canvas(width=800,height=526) #canvas obj allows us to lay things on top of eachother

card_front=PhotoImage(file="images/card_front.png")
new_image=PhotoImage(file="images/card_back.png")
canvas_image=canvas.create_image(400,263,image=card_front) #args are x and y value of that image
card_title=canvas.create_text(400,150,text="",font=("Arieal",40,"italic"))
card_word=canvas.create_text(400,300,text="",font=("Arieal",50,"bold"))
canvas.grid(row=0,column=0,columnspan=2) #to AC show up on the screen, columnspan of 2 means it starts at column 0 but ends at coumlumn 1
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0) #changes flashcard bg color to the one of the window






canvas.grid(row=0,column=0,columnspan=2)
canvas.itemconfig(canvas_image,image=new_image)

wrong_img=PhotoImage(file="images/wrong.png")
right_img=PhotoImage(file="images/right.png")
right_button=Button(image=right_img,highlightthickness=0,command=save_info)
right_button.grid(row=1,column=1)
wrong_button=Button(image=wrong_img,highlightthickness=0,command=next_card)
wrong_button.grid(row=1,column=0)

next_card()









window.mainloop()