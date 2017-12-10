import tkinter
import random


colors = ['Red', 'Blue', 'Green', 'Yellow', 'Orange', 'Pink', 'White', 'Purple', 'Brown' , 'Black']

score = 0;

timeRemaining = 30;


def startGame(event):
    if timeRemaining == 30:
        countDown()

    nextColor()

def nextColor():
    global score
    global timeRemaining

    if timeRemaining > 0:
        #...make the text entry box active.
        e.focus_set()

        #if the colour typed is equal to the colour of the text...
        if e.get().lower() == colors[1].lower():
            #...add one to the score.
            score += 1

        #clear the text entry box.
        e.delete(0, tkinter.END)
        #shuffle the list of colours.
        random.shuffle(colors)
        #change the colour to type, by changing the text _and_ the colour to a random colour value
        displayLabel.config(fg=str(colors[1]), text=str(colors[0]))
        #update the score.
        scoreLabel.config(text="Score: " + str(score))



def countDown():
    #use the globally declared 'play' variable above.
    global timeRemaining

    #if a game is in play...
    if timeRemaining > 0:
        #decrement the timer.
        timeRemaining -= 1
        #update the time left label.
        timeLabel.config(text="Time left: " + str(timeRemaining))
        #run the function again after 1 second.
        timeLabel.after(1000, countDown)

#GUI lol

root = tkinter.Tk()
#set the title.
root.title("Shraddy Game")
#set the size.
root.geometry("800x300")

instructions = tkinter.Label(root, text="Type in the colour of the words, and not the word text!", font=('Helvetica', 12))
instructions.pack()

scoreLabel = tkinter.Label(root, text="Press enter to start", font=('Helvetica', 12))
scoreLabel.pack()

timeLabel = tkinter.Label(root, text="Time left: " + str(timeRemaining), font=('Helvetica', 12))
timeLabel.pack()

displayLabel = tkinter.Label(root, text = "Color will appear here" , font=('Helvetica', 60))
displayLabel.pack()


e = tkinter.Entry(root)
#run the 'startGame' function when the enter key is pressed.
root.bind('<Return>', startGame)
e.pack()
#set focus on the entry box.
e.focus_set()

#start the GUI
root.mainloop()
