# IMPORTS---------------------------------------------------------------------------------------------------------------
import os.path
from os import path
from tkinter.filedialog import askopenfilename
from tkinter import *
import cv2

# CLASS DEFINITIONS-----------------------------------------------------------------------------------------------------
class myVideo(object):

    def __init__(self, fullpath):
        self.fullpath = fullpath
        self.file = os.path.basename(self.fullpath)
        self.path = self.fullpath.replace(self.file, '')
        self.name = self.file.replace('.mp4', '')


# BODY FUNCTIONS--------------------------------------------------------------------------------------------------------

# select video file from directory
def selectVideo():
    Tk().withdraw()
    filename = askopenfilename()

    return filename

# parses the video into individual frames as images
def parseVideo(video):
    # defines path to folder where images will be stored
    folderpath = str(video.path) + str(video.name) + '/'
    print(folderpath)

    # check if folder already exists, if not, makes the folder
    if not(path.exists(folderpath)):
        os.mkdir(folderpath)
    else:
        print("folder already exists")

    vid = cv2.VideoCapture(video.fullpath)
    success, image = vid.read()
    count = 0

    while success:
        # saves every 5th frame of the video
        if count % 5 == 0:
            cv2.imwrite(folderpath + "frame%d.jpg" % count, image)
        success, image = vid.read()
        count += 1

    print("Video parsed")

    return
