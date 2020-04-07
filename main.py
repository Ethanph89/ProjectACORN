# IMPORTS---------------------------------------------------------------------------------------------------------------
import json
from os import rename, remove
import tkinter as tk
from pathlib import Path
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

# MAIN FUNCTION---------------------------------------------------------------------------------------------------------
def main():
    # select video for use and initialize video object
    video = sqVideo.myVideo(sqVideo.selectVideo())
    print("file: " + str(video.fullpath))

    # parse video into images in a folder
    folderpath = sqVideo.parseVideo(video)

    # find all parsed images
    pathlist = Path(folderpath).glob('**/*.jpg')

    # iterate through each image
    for path in pathlist:
        jpgPath = str(path)
        print("jpgPath: " + str(jpgPath))

        # initializes the image object
        image = sqVideo.myImage(jpgPath)

        # create an array of the image pixels
        pixelArray = sqVideo.openJPG(jpgPath)


# BODY FUNCTIONS--------------------------------------------------------------------------------------------------------

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