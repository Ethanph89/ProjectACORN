# IMPORTS---------------------------------------------------------------------------------------------------------------
import PIL.Image
from PIL import Image, ImageFilter, ImageShow
import PIL.Image
import numpy as np
import boto3
import os.path
from os import path
from tkinter.filedialog import askopenfilename
from tkinter import *
import json
import cv2

# CLASS DEFINITIONS-----------------------------------------------------------------------------------------------------
class myVideo(object):

    def __init__(self, fullpath):
        self.fullpath = fullpath
        self.file = os.path.basename(self.fullpath)
        self.path = self.fullpath.replace(self.file, '')
        self.name = self.file.replace('.mp4', '')

class myImage(object):

    def __init__(self, fullpath):
        self.fullpath = fullpath

        # create an array of the image pixels
        self.pixelArray = openJPG(fullpath)

        # find features of image
        self.featuresJSON = rekognitionRequest(fullpath)
        self.awsMasterOutput = parseAWSOutput(self)
        self.xCoord = self.awsMasterOutput[0]
        self.yCoord = self.awsMasterOutput[1]
        self.timestamp = self.awsMasterOutput[2]


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
            cv2.imwrite(folderpath + "frame%05d.jpg" % count, image)
        success, image = vid.read()
        count += 1

    print("Video parsed")

    return folderpath


#   opens JPG and returns RGB pixel array
def openJPG(path):
    im = PIL.Image.open(path)
    pixel_array = np.array(im)

    return pixel_array


#   sends image to rekognition client
def rekognitionRequest(path):
    client = boto3.client('rekognition')

    image = open(path, "rb")

    response = client.detect_labels(
        Image={'Bytes': image.read()}
    )

    image.close()
    print("AWS response: " + str(response))

    return response

#   parses AWS output into an array
def parseAWSOutput(self):
    nameList = ["Animal", "Mammal", "Rodent", "Squirrel", "Rat", "Rabbit", "Bird", "Chicken", "Cat"]
    awsName = None
    awsCoordinates = None
    x = None
    y = None
    time = self.fullpath[-9:].replace('.jpg', '')

    awsData = json.loads(json.dumps(self.featuresJSON))

    # iterate throught labels to find the correct one
    index = 0
    for i in awsData.get("Labels"):
        tempAWSName = awsData.get("Labels")[index].get("Name")
        tempAWSCoordinates = awsData.get("Labels")[index].get("Instances")

        if tempAWSName in nameList and tempAWSCoordinates != []:
            print("found squirrel")
            awsName = tempAWSName
            awsCoordinates = awsData.get("Labels")[index].get("Instances")[0].get("BoundingBox")
            print("awsCoordinates = " + str(awsCoordinates))

            # find x and y coords of squirrel + timestamp
            left = awsCoordinates.get("Left")
            width = awsCoordinates.get("Width")
            top = awsCoordinates.get("Left")
            height = awsCoordinates.get("Height")
            x = left + (width/2)
            y = top + (height/2)

            break
        elif tempAWSCoordinates != []:
            print("coord name: " + str(tempAWSName))

        index = index + 1

    if awsName == None or awsCoordinates == None:
        awsName = "none"
        awsCoordinates = "none"

    print("awsName: " + str(awsName))
    print("awsCoord: " + str(awsCoordinates))

    print("x: " + str(x))
    print("y: " + str(y))
    print("time: " + str(time))

    return x, y, time

def saveData(folder, image):
    d = open("data.csv", "a")
    d.write(str(image.fullpath[-14:]) + ',' + str(image.xCoord) + ',' + str(image.yCoord) + ',' + str(image.timestamp) + '\n')
    d.close()