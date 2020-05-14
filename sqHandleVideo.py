# AUTHORS:
# Ethan Hunt
# IMPORTS---------------------------------------------------------------------------------------------------------------
from pathlib import Path
import sqVideo
from datetime import datetime

# UPLOAD----------------------------------------------------------------------------------------------------------------
def handleVideo():
    # select video for use and initialize video object
    videoCheck = "nofile"

    while videoCheck == "nofile":
        video = sqVideo.myVideo(sqVideo.selectVideo())
        print(video.fullpath)
        videoCheck = video.fullpath

    if videoCheck == "":
        return

    print("file: " + str(video.fullpath))

    # parse video into images in a folder
    folderpath = sqVideo.parseVideo(video)

    # create CSV for saving data
    f = open("data" + video.name + ".csv", "w")
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
            sqVideo.saveData(video, image)