# AUTHORS:
# Giancarlo Garcia Deleon, Andrew Bhatti, Ethan Hunt
# IMPORTS---------------------------------------------------------------------------------------------------------------
import glob
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import os
from datetime import datetime


# CLASS DEFINITIONS-----------------------------------------------------------------------------------------------------
class myTimeline(object):

    def __init__(self):
        self.fig = self.genFig()
        self.ax = self.toAx()
        self.x1 = []
        self.y = []
        self.z = []

    def genFig(self):
        return pyplot.figure()

    def toAx(self):
        return Axes3D(self.fig)


class myTimelineUnit(object):

    def __init__(self):
        self.x1 = []
        self.y = []
        self.z = []

# BODY FUNCTIONS--------------------------------------------------------------------------------------------------------

def generateTimelineOne(x):
    print("Directory: " + x)

    # final_directory = os.path.join(currdir, r'new_folder')
    if not os.path.exists("saves"):
        os.makedirs("saves")
        print("Created new directory for new scatterplots.")
    else:
        print("Directory to save new scatterplots already exists.\n")

    print("NOW GENERATING SCATTERPLOTS")

    df = pd.read_csv(x, delimiter=',', header=1)

    timeline = myTimeline()

    print("NOW GENERATING SCATTERPLOT", x)

    # append data to timeline arrays
    for i, row in df.iterrows():
        timeline.x1.append(float(row.values[1]))  # x should be time. so we name it Z, in place of x
        timeline.y.append(float(row.values[2]))  # note that '2' is the column in which the iteration occurs
        timeline.z.append(float(row.values[3]))

    timeline.ax.scatter(timeline.z, timeline.x1, timeline.y, '-o')

    # set axis labels
    timeline.ax.set_zlabel('Z Coordinates')
    timeline.ax.set_ylabel('Y Coordinates')
    timeline.ax.set_xlabel('TIME(X)')
    timeline.ax.plot(timeline.z, timeline.x1, timeline.y, color='r', lw=1)  # lw is line width

    # Use complete datetime as a unique filename
    now = str(datetime.now()).replace(' ', '').replace(':', '').replace('.', '').replace('-', '')

    print(now)
    timeline.fig.savefig('saves/' + "time" + now + '.png', dpi=1000, bbox_inches='tight', transparent=True)
    print("SCATTERPLOT", x, "GENERATED\n")
    timeline.ax.cla()

    return

def generateTimelineUnit(x):
    df = pd.read_csv(x, delimiter=',', header=1)

    timeline = myTimelineUnit()

    # append data to timeline arrays
    for i, row in df.iterrows():
        timeline.x1.append(float(row.values[1]))  # x should be time. so we name it Z, in place of x
        timeline.y.append(float(row.values[2]))  # note that '2' is the column in which the iteration occurs
        timeline.z.append(float(row.values[3]))

    return timeline.x1
