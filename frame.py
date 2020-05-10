# AUTHOR:
# Andrew Bhatti
# GUI Interface

import tkinter as draw
from tkinter import *
import tkinter.font as font
from PIL import Image, ImageTk
import os
import os.path
import shutil
import sys
import random
import csv
from main import handleVideo
import sqVideo
import sqHeatmap
import sqTimeline

# CLASS DEFINITIONS-----------------------------------------------------------------------------------------------------

# todo classes:
#  loadedCSV
#  heatmap
#  timeline


# INITIALIZATION------------------------------------------------------------------------------------------INITIALIZATION
gui = draw.Tk()
gui.iconphoto(False, draw.PhotoImage(file="assets/ico_acorn.png"))
gui.geometry("875x600+540+200")
gui.title("A.C.O.R.N.")
gui.resizable(False, False)

# FONTS------------------------------------------------------------------------------------------------------------FONTS
cleanFont = font.Font(family='Helvetica', size=12)

# GRAPHICS------------------------------------------------------------------------------------------------------GRAPHICS
btn = Image.open("assets/bg_button_rect_red.png")
btn = btn.resize((round(278 * 0.55), round(61 * 0.55)), Image.ANTIALIAS)
btn = ImageTk.PhotoImage(btn)  # resized and formatted graphic


holder = Image.open("assets/acorn_main.png")
holder = holder.resize((300, 300), Image.ANTIALIAS)
holder = ImageTk.PhotoImage(holder)

# FRAMES - - - Top, Left, Right-----------------------------------------------------------------------------------FRAMES
banner = Frame(gui,
               bd=3,
               cursor="spider",
               bg="#4b636e",
               relief="groove")

interface = Frame(gui,
                  bd=3,
                  cursor="trek",
                  bg="#78909c",
                  relief="groove")  # left side - houses buttons / interaction

display = Frame(gui,
                bd=3,
                cursor="dotbox",
                bg="#a7c0cd",
                relief="groove")  # right side - houses graphs


# showFile = LabelFrame(interface,
#                      text="UPLOAD",
#                      fg="black",
#                      bd=2,
#                      relief="flat")
# showFile.pack(padx=30, pady=(15, 15))


# STARTUP DETAIL-------------------------------------------------------------------------------------------------STARTUP
greeting = "Welcome to Project A.C.O.R.N. \n\n" \
           "This application uses video files to create graphics for visual\n" \
           "representation. This tool serves as a time-efficient, objective visualization of data."

headline = Label(banner,
                 text=greeting,
                 bg="#4b636e",
                 font=cleanFont,
                 fg='white')

art = Label(display,
            image=holder,
            bd=0,
            bg="#a7c0cd")


# canvas = draw.Canvas(interface, width=54, height=54, highlightthickness=0, bg="red")
# canvas.pack()
# canvas.background = bdSq
# canvas.create_image(0, 0, anchor=draw.NW, image=bdSq)

# BUTTONS--------------------------------------------------------------------------------------------------------BUTTONS
uploadVideo = Button(interface,
                     image=btn,
                     highlightthickness=0,
                     compound=CENTER,
                     text="Upload Video",
                     font=cleanFont,
                     bd=0,
                     relief="flat",
                     bg="#78909c",
                     activebackground="#78909c",
                     command=lambda: operation("upload"))

useFile = Button(interface,
                 image=btn,
                 highlightthickness=0,
                 compound=CENTER,
                 text="Import CSV",
                 font=cleanFont,
                 bd=0,
                 relief="flat",
                 bg="#78909c",
                 activebackground="#78909c",
                 command=lambda: operation("use"))

generate = Button(interface,
                  image=btn,
                  highlightthickness=0,
                  compound=CENTER,
                  text="Generate Graphs",
                  font=cleanFont,
                  bd=0,
                  relief="flat",
                  bg="#78909c",
                  activebackground="#78909c",
                  command=lambda: operation("graph"))


# INFORMATION DISPLAY----------------------------------------------------------------------------------------INFORMATION
filename = Label(interface,
                 text="CSV files detected: \n",
                 font=cleanFont,
                 width=18, height=4,
                 relief="groove",
                 bg="#a7c0cd")

messages = LabelFrame(interface,
                      text="Description",
                      font=cleanFont,
                      fg="black",
                      bd=2,
                      relief="raised",
                      bg="#78909c")

info = "Getting Started: \n\n " \
       "1) Upload a local video file. \n " \
       "2) Add any additional .csv \n " \
       "3) Begin graph generation."

text = Label(messages,
             text=info,
             font=cleanFont,
             width=28, height=18,
             relief="groove",
             bg="#a7c0cd")  # dynamically updated per lambda


# FUNCTIONS----------------------------------------------------------------------------------------------------FUNCTIONS

def main():
    gui.mainloop()


def detective():  # Searches for CSV files
    bucket = []
    for datafile in os.listdir():
        if datafile.endswith(".csv"):
            print(datafile)
            bucket.append(datafile)
            # filename.config(text=datafile)
            continue
    if not bucket:
        return "No CSV files detected."
    else:
        # bucket = (*bucket, sep= "\n")
        return view(bucket)


def view(bucket):
    for i in range(len(bucket)):
        filename.config(text=filename.cget("text") + "\n" + bucket[i])


def operation(self):
    print("I received: " + self)  # debugging
    event = ""  # to be packed into description
    if self == 'upload':  # UPLOAD VIDEO OPTION
        event = "Please select a file for upload."
        text.configure(text=event)
        package()
        print(event)  # debugging
        handleVideo()

    elif self == 'use':  # USE FILE OPTION
        event = "Please select a .csv file."
        text.configure(text=event)
        package()
        print(event)  # debugging

    elif self == 'graph':  # GENERATE GRAPHS
        event = "A graph is being generated \n with the provided data." \
                "\n\n Please Wait . . ."
        text.configure(text=event)
        package()
        print(event)  # debugging
        sqTimeline.generateTimeline()
        artshow()  # hang that art on the wall

    else:  # what did you break
        print("Uncaught error has occurred.")


def package():
    text.pack()
    text.update()


def artshow():
    for imgfile in os.listdir("saves"):
        if imgfile.endswith(".png"):
            print("Found the image! " + imgfile)  # debugging
            patchwork(imgfile)
            art.update()
            text.configure(text=":D")
            package()
        else:
            print("ERROR: No images exist.")


def patchwork(file):
    print("saves/" + file)
    graph = Image.open("saves/" + file)
    graph = graph.resize((530, 370), Image.ANTIALIAS)
    graph = ImageTk.PhotoImage(graph)  # resized and formatted graphic
    art.configure(image=graph)
    art.image = graph
    art.pack()

# ARRANGEMENT------------------------------------------------------------------------------------------------ARRANGEMENT
### THE ORDER IN WHICH ITEMS ARE PACKED IS IMPORTANT ###
###### FRAME: BANNER ######
banner.pack(side=TOP, fill="x")

headline.pack(fill='x', pady=15)        # headlining text

###### FRAME: INTERFACE ######
interface.pack(side=LEFT, fill='x')

uploadVideo.pack(pady=(28, 10))         # upload video file button
useFile.pack(pady=10)                   # upload csv file button
filename.pack(padx=20, pady=10)                  # displays csv files

generate.pack(pady=15)                  # generate graphs button

messages.pack(padx=30, pady=(15, 30))   # description/info box
text.pack()                             # text inside desc/info box

###### FRAME: DISPLAY ######
display.pack(side=RIGHT, fill=BOTH, expand=YES)

art.pack(fill=BOTH, expand=YES)         # graphical display

# SHOWTIME------------------------------------------------------------------------------------------------------SHOWTIME
filename.config(text=detective())
#detective()
main()
