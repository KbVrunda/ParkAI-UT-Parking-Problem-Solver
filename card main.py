from tkinter import*
import random

#creating the window
window = Tk()
window.title("TicTacToe")

#Canvas widget: enables us to display graphics
canvas = Canvas(window, width = 336, height = 360)
imageX = PhotoImage(file = "/Users/vrundapatel/Documents/BME303/X.gif")
imageO = PhotoImage(file = "/Users/vrundapatel/Documents/BME303/O.gif")

coordinate_values = [0, 112, 224]
canvas.pack()

for x in coordinate_values:
    for y in coordinate_values:
        num = random.randint(0, 1)
        if(num == 1):
            canvas.create_image(x, y, anchor=NW, image = imageX)
            #Anchors are used to define where text is positioned relative to a reference point
        else:
            canvas.create_image(x, y, anchor = NW, image = imageO)

window.mainloop() #tells python to run the Tkinter event loop