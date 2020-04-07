# IMPORTS---------------------------------------------------------------------------------------------------------------
import json
from os import rename, remove
import PIL.Image
from PIL import Image, ImageFilter, ImageShow
import PIL.Image
import numpy as np
import boto3
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
#  image
#  loadedCSV
#  heatmap
#  timeline

# MAIN FUNCTION---------------------------------------------------------------------------------------------------------
def main():
    # select video for use
    video = sqVideo.myVideo(sqVideo.selectVideo())
    print("file: " + str(video.fullpath))

    # parse video into images in a folder
    sqVideo.parseVideo(video)


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