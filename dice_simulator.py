import tkinter   #import tkinter for gui
import random    #import random module for generating random number
core = tkinter.Tk()    #calling tkinter function into core variable
core.geometry('600x400')    #using .geometry from tk() for screen size
core.title('Roll the Dice')    #giving a title for gui
display = tkinter.Label(core, text='', font=('Impact', 260))    #body for gui
def roll_the_dice():    #created a function for rolling the dice with random number
    dice = [1,2,3,4,5,6]    #inserting values from 1 to 6 into an array
    display.configure(text=f'{random.choice(dice)}    {random.choice(dice)}')    #printing random values from array
    display.pack()    #creating a widgets
button = tkinter.Button(core, text='Roll the Dice', foreground='red', command=roll_the_dice)    #creating a button for function
button.pack()    #creating a widgets
core.mainloop()    #stay inside the loop
