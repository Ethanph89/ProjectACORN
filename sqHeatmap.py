# AUTHOR:
# Cassandra Olivas
# IMPORTS---------------------------------------------------------------------------------------------------------------
import os
import matplotlib.patheffects as PathEffects
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style, pyplot
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
from datetime import datetime


# CLASS DEFINITIONS-----------------------------------------------------------------------------------------------------
class myHeatmap(object):

    def __init__(self):
        self.x1 = []
        self.y = []
        self.xLabel = "X axis"
        self.yLabel = "Y axis"

# BODY FUNCTIONS--------------------------------------------------------------------------------------------------------

def generateHeatmap(csvfile):

    print("Directory: " + csvfile)
    if not os.path.exists("saves"):
        os.makedirs("saves")
        print("Created new directory for new heatmaps.")
    else:
        print("Directory to save new heatmaps already exists.\n")

    df = pd.read_csv(csvfile, delimiter=',', header=1)

    # initialize heatmap object
    heatmap = myHeatmap()

    print("NOW GENERATING HEATMAP", csvfile)
    for i, row in df.iterrows():
        heatmap.x1.append(float(row.values[1]))  # x should be time. so we name it Z, in place of x
        heatmap.y.append(float(row.values[2]))  # note that '2' is the column in which the iteration occurs

    plt.hist2d(heatmap.x1, heatmap.y, bins=30, cmap='Blues', alpha=0.7)
    cb = plt.colorbar()
    x = "Counts in Bin"
    cb.set_label(x)

    plt.title('Data from the CSV File: X and Y Locations', color='black')

    plt.xlabel(heatmap.xLabel, color='black')
    plt.ylabel(heatmap.yLabel, color='black')

    # use complete datetime as a unique filename with cleaned up string
    now = str(datetime.now()).replace(' ', '').replace(':', '').replace('.', '').replace('-', '')

    plt.savefig('saves/' + "heat" + now + '.png', dpi=300, transparent=True)
    print("HEATMAP", csvfile, "GENERATED\n")

    # Clears the color bar upon a new plt, All axes definitions are reset
    plt.clf()

    return

def generateHeatmapUnit(csvfile):

    df = pd.read_csv(csvfile, delimiter=',', header=1)

    heatmap = myHeatmap()

    for i, row in df.iterrows():
        heatmap.x1.append(float(row.values[1]))  # x should be time. so we name it Z, in place of x
        heatmap.y.append(float(row.values[2]))  # note that '2' is the column in which the iteration occurs

    return heatmap.x1