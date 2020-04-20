import tkinter as draw
from tkinter.filedialog import askopenfilename
from tkinter import *
import tkinter.font as font
from PIL import Image, ImageTk
from tkinter import ttk
import time
import os
import sys

# Initialization
gui = draw.Tk()
gui.iconphoto(False, draw.PhotoImage(file="bin/ico_acorn.png"))
gui.geometry("800x600")
gui.title("A.C.O.R.N.")

# FONTS
cleanFont = font.Font(family='Helvetica', size=12)

# GRAPHICS
img = Image.open("bin/bg_button_rect_red.png")
img = img.resize((round(278 * 0.55), round(61 * 0.55)), Image.ANTIALIAS)
fit = ImageTk.PhotoImage(img)  # resized and formatted graphic
holder = Image.open("bin/acorn_main.png")
holder = ImageTk.PhotoImage(holder)


# FRAMES - - - Top, Left, Right
welcome = Frame(gui, bd=3, cursor="spider", bg="#4b636e", relief="groove")
welcome.pack(side=TOP, fill="x")
greeting = "Welcome to Project A.C.O.R.N. \n\n" \
           "This application uses video files to create graphics for visual\n" \
           "representation. This tool serves as a time-efficient, objective visualization of data."
headline = Label(welcome, text=greeting, bg="#4b636e", font=cleanFont, fg='white')
headline.pack(fill='x', pady=15)  # headlining text
interface = Frame(gui, bd=3, cursor="trek", bg="#78909c", relief="groove")  # left side - houses buttons / interaction
interface.pack(side=LEFT, fill='x')
display = Frame(gui, bd=3, cursor="dotbox", bg="#a7c0cd", relief="groove")  # right side - houses graphs
display.pack(side=RIGHT, fill=BOTH, expand=YES)

# GRAPHS DISPLAY
test = Label(display, image=holder, bd=0, bg="#a7c0cd")
test.pack()


# FUNCTIONS


def operation(self):
    print("I received: " + self)  # debugging
    if self == 'use':  # USE FILE OPTION
        print("You want to use a previous file.")

    elif self == 'upload':  # UPLOAD VIDEO OPTION
        print("Please selected a file for upload.")
        os.system('python main.py')

    elif self == 'graph':  # GENERATE GRAPHS
        print("The graphs will now be generated.")
        os.system('python multinput.py')

    else:  # what did you break
        print("Uncaught error has occurred.")


def informed():
    result = "stuff"
    text.insert(INSERT, result)
    print(result)


# BUTTONS
uploadVideo = Button(interface,
                     image=fit,
                     compound=CENTER,
                     text="Upload Video",
                     bd=0,
                     relief="flat",
                     bg="#78909c",
                     activebackground="#78909c",
                     command=lambda: operation("upload"))
uploadVideo['font'] = cleanFont
uploadVideo.pack(pady=(30, 15))

useFile = Button(interface,
                 image=fit,
                 compound=CENTER,
                 text="Use File",
                 bd=0,
                 relief="flat",
                 bg="#78909c",
                 activebackground="#78909c",
                 command=lambda: operation("use"))
useFile['font'] = cleanFont
useFile.pack(pady=15)

generate = Button(interface,
                  image=fit,
                  compound=CENTER,
                  text="Generate Graphs",
                  bd=0,
                  relief="flat",
                  bg="#78909c",
                  activebackground="#78909c",
                  command=lambda: operation("graph"))
generate['font'] = cleanFont
generate.pack(pady=15)

# INFORMATION DISPLAY
messages = LabelFrame(interface,
                      text="Description",
                      bd=2,
                      relief="raised",
                      bg="#78909c")
messages['font'] = cleanFont
messages.pack(padx=30, pady=(15, 30))
text = Text(messages, width=28, relief="groove", bg="#a7c0cd")
text.pack()

# Let's start the show - - - - - - - - - - - - - - - - -
gui.mainloop()
