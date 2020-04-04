# IMPORTS---------------------------------------------------------------------------------------------------------------
import json
from os import rename, remove
import os.path
import PIL.Image
from PIL import Image, ImageFilter, ImageShow
import PIL.Image
import numpy as np
import boto3
import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import *
from pathlib import Path
import shutil
import sys
import random
import csv
import cv2

# CLASS DEFINITIONS-----------------------------------------------------------------------------------------------------
class myVideo(object):

    def __init__(self, file):
        self.file = file

# todo classes:
#  image
#  loadedCSV
#  heatmap
#  timeline

# MAIN FUNCTION---------------------------------------------------------------------------------------------------------
def main():
    video = myVideo(selectVideo)
    print("file: " + str(video.file))

    parseVideo(video)


# BODY FUNCTIONS--------------------------------------------------------------------------------------------------------

# select video file from directory
def selectVideo():
    Tk().withdraw()
    filename = askopenfilename()

    return filename

# parses the video into individual frames as images
def parseVideo(video):
    # todo:
    #  create dynamic directory for images to save into
    #  make video link dynamic

    vid = cv2.VideoCapture("testVid.mp4")
    success, image = vid.read()
    count = 0
    while success:
        # saves every 5th frame of the video
        if count % 5 == 0:
            cv2.imwrite("testVid/" + "frame%d.jpg" % count, image)
        success, image = vid.read()
        count += 1

    print("Video parsed")

    return

# todo functions:
#  parse video to images
#  send image to API
#  save data to CSV
#  select graph
#  generate graph
#  display graph
#  import CSV

# RUN MAIN--------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    main()