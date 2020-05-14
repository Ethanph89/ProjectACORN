# AUTHOR:
# Andrew Bhatti
# GUI Interface & Functionality

import tkinter as draw
from tkinter import *
import tkinter.font as font
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
import os
import os.path
import glob
import ntpath
from sqHandleVideo import handleVideo
from sqTimeline import generateTimelineOne
from sqHeatmap import generateHeatmap

# INITIALIZATION------------------------------------------------------------------------------------------INITIALIZATION
gui = draw.Tk()
gui.iconphoto(False, draw.PhotoImage(file="assets/ico_acorn.png"))
gui.geometry("875x575+540+200")
gui.title("A.C.O.R.N.")
gui.resizable(False, False)
ghost = "wandering"

# FONTS------------------------------------------------------------------------------------------------------------FONTS
cleanFont = font.Font(family='Helvetica', size=12)

# GRAPHICS------------------------------------------------------------------------------------------------------GRAPHICS
btn = Image.open("assets/bg_button_rect_red.png")
btn = btn.resize((round(278 * 0.55), round(61 * 0.55)), Image.ANTIALIAS)
btn = ImageTk.PhotoImage(btn)  # resized and formatted graphic

holder = Image.open("assets/acorn_main.png")
holder = holder.resize((300, 300), Image.ANTIALIAS)
holder = ImageTk.PhotoImage(holder)

# FRAMES----------------------------------------------------------------------------------------------------------FRAMES
banner = Frame(gui,
               bd=3,
               cursor="spider",
               bg="#4b636e",
               relief="groove")     # TOP justify; contains welcome info / i

interface = Frame(gui,
                  bd=3,
                  cursor="trek",
                  bg="#78909c",
                  relief="groove")  # LEFT justify; contains buttons / interaction

display = Frame(gui,
                bd=3,
                cursor="dotbox",
                bg="#a7c0cd",
                relief="groove")    # RIGHT justify; contains images / graphs

options = Frame(interface,
                bd=1,
                bg="#a7c0cd",
                relief="groove")    # Contains radio buttons Video / CSV

shell = Frame(interface,
              bd=0,
              bg="#a7c0cd",
              relief="flat")        # Space to swap between two buttons

checkboxes = Frame(interface,
                   bd=1,
                   bg="#a7c0cd",
                   relief="groove")  # Contains checkboxes hmap / tline

purpose = Frame(interface,
                bd=0,
                bg="#a7c0cd",
                relief="flat")      # Contains generate button / extra

messages = Frame(interface,
                 bd=1,
                 relief="groove",
                 bg="#a7c0cd")      # Contains information relevant to user

# STARTUP DETAIL-------------------------------------------------------------------------------------------------STARTUP
greeting = "Welcome to Project A.C.O.R.N. \n\n" \
           "An open-source software used to quantify animal behavior. It uses a 2D coordinate system\n" \
           "and time to provide heat plots based on location frequency and scatter plots based on location at each time."

headline = Label(banner,
                 text=greeting,
                 bg="#4b636e",
                 font=cleanFont,
                 fg='white')        # Headlining text at top of window

art = Label(display,
            image=holder,
            bd=0,
            bg="#a7c0cd",
            highlightthickness=0,
            borderwidth=0)          # Image container

# BUTTONS--------------------------------------------------------------------------------------------------------BUTTONS
a = draw.IntVar()
a.set(1)
left = Radiobutton(options,
                   text="Video",
                   indicatoron=0,
                   bg="#a92d2d",
                   font=cleanFont,
                   width=10,
                   padx=20,
                   variable=a,
                   value=1,
                   command=lambda: choice())

right = Radiobutton(options,
                    text="CSV",
                    indicatoron=0,
                    bg="#a92d2d",
                    font=cleanFont,
                    width=10,
                    padx=20,
                    variable=a,
                    value=2,
                    command=lambda: choice())

uploadVideo = Button(shell,
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

useFile = Button(shell,
                 image=btn,
                 highlightthickness=0,
                 compound=CENTER,
                 text="Select CSV",
                 font=cleanFont,
                 bd=0,
                 relief="flat",
                 bg="#78909c",
                 activebackground="#78909c",
                 command=lambda: operation("use"))

generate = Button(purpose,
                  image=btn,
                  highlightthickness=0,
                  compound=CENTER,
                  text="Generate Graph",
                  font=cleanFont,
                  bd=0,
                  relief="flat",
                  bg="#78909c",
                  activebackground="#78909c",
                  state=DISABLED,
                  command=lambda: operation("graph"))

heatchk = IntVar()
timechk = IntVar()
hotmap = Checkbutton(checkboxes,
                     text="Heatmap",
                     font=cleanFont,
                     bg="#a92d2d",
                     width=12,
                     variable=heatchk,
                     onvalue=1,
                     offvalue=0,
                     state=DISABLED,
                     command=lambda: operation("hmap"))

history = Checkbutton(checkboxes,
                      text="Timeline",
                      font=cleanFont,
                      bg="#a92d2d",
                      width=12,
                      variable=timechk,
                      onvalue=1,
                      offvalue=0,
                      state=DISABLED,
                      command=lambda: operation("tline"))


# INFORMATION DISPLAY---------------------------------------------------------------------------------------------------
filename = Label(interface,
                 text="No CSV file present.",
                 wraplength=230,
                 font=cleanFont,
                 width=26, height=1,
                 relief="groove",
                 bd=1,
                 bg="#a7c0cd")              # Location displays file name

info = "Getting Started: \n\n " \
       "·• Upload a local video file. \n " \
       "·• Add any additional CSV files"

text = Label(messages,
             text=info,
             font=cleanFont,
             wraplength=240,
             anchor=CENTER,
             width=28, height=5,
             relief="flat",
             bg="#a7c0cd")                  # dynamically updated per lambda


# FUNCTIONS----------------------------------------------------------------------------------------------------FUNCTIONS
def main():
    print("Ghost is " + ghost)  # debugging
    choice()
    detective()
    gui.mainloop()


def choice():
    # print(a.get())
    if a.get() == 1:    # enable Video btn
        useFile.pack_forget()
        uploadVideo.pack()
    else:
        uploadVideo.pack_forget()
        useFile.pack()


def detective():    # Search current directory for newest CSV file
    try:
        csvfile = max(glob.iglob('*.csv'), key=os.path.getctime)  # get recent CSV file
        unlock()
        print("Most recent CSV: " + csvfile)
        filename.config(text="Loaded: " + csvfile)
    except (ValueError, TypeError):
        print("No CSV files present in cwd.")
    # print(ghost)    # debugging


def selection():
    if (heatchk.get() == 1) & (timechk.get() == 0) & (ghost != "wandering"):
        print("Heat is selected only")
        generate.configure(state=NORMAL)
    elif (heatchk.get() == 0) & (timechk.get() == 1) & (ghost != "wandering"):
        print("Time is selected only")
        generate.configure(state=NORMAL)
    elif (heatchk.get() == 1) & (timechk.get() == 1) & (ghost != "wandering"):
        print("Heat & Time are selected.")
        generate.configure(state=NORMAL)
    else:
        generate.configure(state=DISABLED)


def unlock():
    hotmap.config(state=NORMAL)
    history.config(state=NORMAL)


def operation(self):
    csvfile = ""
    print("I received: " + self)    # debugging
    event = ""  # to be packed into description
    if self == 'upload':    # UPLOAD VIDEO OPTION
        event = "Select your video file. \n Data is being processed. \n\n Please Wait. . ."
        text.configure(text=event)
        package()
        print(event)    # debugging
        handleVideo()
        detective()
        if ghost != "wandering":
            unlock()

    elif self == 'use':  # USE FILE OPTION
        event = "Please select a CSV file."
        text.configure(text=event)
        package()

        print(event)    # debugging
        locator()
        csvfilename = ntpath.basename(ghost)
        filename.config(text="Loaded: " + csvfilename)
        unlock()

    elif self == 'tline' or self == 'hmap':
        print("A tickbox has been hit")
        selection()

    elif self == 'graph':   # GENERATE GRAPHS
        print(csvfile)
        event = "A graph is being generated \n with the provided data." \
                "\n\n Please Wait . . ."
        text.configure(text=event)
        package()
        print(event)    # debugging

        if timechk.get() == 1 and heatchk.get() == 0:
            generateTimelineOne(ghost)
            artshow()   # hang that art on the wall
        elif heatchk.get() == 1 and timechk.get() == 0:
            generateHeatmap(ghost)
            artshow()
        elif timechk.get() == 1 and heatchk.get() == 1:
            generateHeatmap(ghost)
            generateTimelineOne(ghost)
            artshow()
            print("Two graph image are being generated.")
        else:
            print("This should not be possible.")

    else:   # what did you break
        print("Uncaught error has occurred.")


def locator():
    global ghost
    ghost = askopenfilename()
    print("Ghost now knows: " + ghost)
    return ghost


def package():
    text.pack()
    text.update()


def artshow():
    imgfile = max(glob.iglob('saves/*.png'), key=os.path.getctime)  # get recent PNG file
    print("Found the image! " + imgfile)    # debugging
    patchwork(imgfile)
    art.update()
    text.configure(text="Graph Generated  >")
    package()


def patchwork(file):
    print(file)
    graph = Image.open(file)
    graph = graph.resize((530, 370), Image.ANTIALIAS)
    graph = ImageTk.PhotoImage(graph)   # resized and formatted graphic
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

options.pack(side=TOP, pady=(20, 10))   # radio buttons
left.pack(side=LEFT)
right.pack(side=RIGHT)

shell.pack(side=TOP, pady=(10, 15))     # contains buttons Upload / Select

filename.pack(padx=20, pady=10)         # displays csv files

checkboxes.pack(side=TOP, pady=(20, 10))    # contains checkboxes hotmap / history
hotmap.pack(side=LEFT)
history.pack(side=LEFT)

purpose.pack(pady=(15, 20))
generate.pack(side=LEFT)                # generate graphs button
# marathon.pack(side=LEFT)

messages.pack(side=BOTTOM, padx=30, pady=(30, 30))  # description/info box
text.pack()

###### FRAME: DISPLAY ######
display.pack(side=RIGHT, fill=BOTH, expand=YES)

art.pack(fill=BOTH, expand=YES)         # graphical display

# SHOWTIME--------------------------------------------------------------------------------------------------------------
main()