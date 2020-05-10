# AUTHORS:
# Andrew Bhatti Tkinter Interface
# Ethan Hunt Upload Video functions
# IMPORTS---------------------------------------------------------------------------------------------------------------
import json
from os import rename, remove
import tkinter as draw
from tkinter import *
import tkinter.font as font
from PIL import Image, ImageTk
import os
from pathlib import Path
import os.path
import shutil
import sys
import random
import csv
import sqVideo
import sqHeatmap
import sqTimeline

# CLASS DEFINITIONS-----------------------------------------------------------------------------------------------------

# todo classes:
#  loadedCSV
#  heatmap
#  timeline

# TKINTER---------------------------------------------------------------------------------------------------------------

# INITIALIZATION ===================================================
gui = draw.Tk()
gui.iconphoto(False, draw.PhotoImage(file="assets/ico_acorn.png"))
gui.geometry("875x500")
gui.title("A.C.O.R.N.")

# FONTS ============================================================
cleanFont = font.Font(family='Helvetica', size=12)

# GRAPHICS =========================================================
img = Image.open("assets/bg_button_rect_red.png")
img = img.resize((round(278 * 0.55), round(61 * 0.55)), Image.ANTIALIAS)
fit = ImageTk.PhotoImage(img)  # resized and formatted graphic
holder = Image.open("assets/acorn_main.png")
holder = holder.resize((300, 300), Image.ANTIALIAS)
holder = ImageTk.PhotoImage(holder)

# FRAMES - - - Top, Left, Right ====================================
banner = Frame(gui,
               bd=3,
               cursor="spider",
               bg="#4b636e",
               relief="groove")
banner.pack(side=TOP, fill="x")

interface = Frame(gui,
                  bd=3,
                  cursor="trek",
                  bg="#78909c",
                  relief="groove")  # left side - houses buttons / interaction
interface.pack(side=LEFT, fill='x')

display = Frame(gui,
                bd=3,
                cursor="dotbox",
                bg="#a7c0cd",
                relief="groove")  # right side - houses graphs
display.pack(side=RIGHT, fill=BOTH, expand=YES)

# STARTUP DETAIL ==================================================
greeting = "Welcome to Project A.C.O.R.N. \n\n" \
           "This application uses video files to create graphics for visual\n" \
           "representation. This tool serves as a time-efficient, objective visualization of data."

headline = Label(banner,
                 text=greeting,
                 bg="#4b636e",
                 font=cleanFont,
                 fg='white')
headline.pack(fill='x', pady=15)  # headlining text

art = Label(display, image=holder, bd=0, bg="#a7c0cd")
art.pack(fill=BOTH, expand=YES)  # placeholder graphic

# BUTTONS  =========================================================
uploadVideo = Button(interface,
                     image=fit,
                     compound=CENTER,
                     text="Upload Video",
                     font=cleanFont,
                     bd=0,
                     relief="flat",
                     bg="#78909c",
                     activebackground="#78909c",
                     command=lambda: operation("upload"))

uploadVideo.pack(pady=(30, 15))

useFile = Button(interface,
                 image=fit,
                 compound=CENTER,
                 text="Use File",
                 font=cleanFont,
                 bd=0,
                 relief="flat",
                 bg="#78909c",
                 activebackground="#78909c",
                 command=lambda: operation("use"))
useFile.pack(pady=15)

generate = Button(interface,
                  image=fit,
                  compound=CENTER,
                  text="Generate Graphs",
                  font=cleanFont,
                  bd=0,
                  relief="flat",
                  bg="#78909c",
                  activebackground="#78909c",
                  command=lambda: operation("graph"))
generate.pack(pady=15)

# INFORMATION DISPLAY ==============================================
messages = LabelFrame(interface,
                      text="Description",
                      font=cleanFont,
                      fg="black",
                      bd=2,
                      relief="raised",
                      bg="#78909c")
messages.pack(padx=30, pady=(15, 30))

info = "Getting Started: \n\n 1) Upload a local video file. \n 2) Add any additional .csv \n 3) Begin graph generation."

text = Label(messages,
             text=info,
             font=cleanFont,
             width=28, height=18,
             relief="groove",
             bg="#a7c0cd")

text.pack()  # dynamically updated per lambda

# MAIN FUNCTION---------------------------------------------------------------------------------------------------------
def main():
    gui.mainloop()

# BODY FUNCTIONS--------------------------------------------------------------------------------------------------------

# TKINTER
def operation(self):
    print("I received: " + self)  # debugging
    event = ""  # to be packed into description
    if self == 'upload':  # UPLOAD VIDEO OPTION
        event = "Please select a file for upload."
        text.configure(text=event)
        package()
        print(event)  # debugging
        uploadVideo()

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
    for file in os.listdir("saves"):
        if file.endswith(".png"):
            print("Found the image! " + file)  # debugging
            patchwork(file)
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

# UPLOAD
def uploadVideo():
    # select video for use and initialize video object
    video = sqVideo.myVideo(sqVideo.selectVideo())
    print("file: " + str(video.fullpath))

    # parse video into images in a folder
    folderpath = sqVideo.parseVideo(video)

    # create CSV for saving data
    f = open("data.csv", "w")
    f.write('image,' + 'x,' + 'y,' + 'time' '\n')
    f.close()

    # find all parsed images
    pathlist = sorted(Path(folderpath).glob('**/*.jpg'))

    # iterate through each image
    for path in pathlist:
        jpgPath = str(path)
        print("jpgPath: " + str(jpgPath))

        # initializes the image object
        image = sqVideo.myImage(jpgPath)

        # if image has features, collects and stores data
        if image.featuresJSON != 0:

            # save data to CSV
            sqVideo.saveData(folderpath, image)


# todo functions:
#  select graph
#  import CSV

# RUN MAIN--------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    main()