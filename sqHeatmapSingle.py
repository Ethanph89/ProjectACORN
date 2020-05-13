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


# style.use('ggplot')

# CLASS DEFINITIONS-----------------------------------------------------------------------------------------------------


# BODY FUNCTIONS--------------------------------------------------------------------------------------------------------

def generateHeatmap(csvfile):
    # x = "dying.csv"
    print("Directory: " + csvfile)
    if not os.path.exists("saves"):
        os.makedirs("saves")
        print("Created new directory for new heatmaps.")
    else:
        print("Directory to save new heatmaps already exists.\n")

    df = pd.read_csv(csvfile, delimiter=',', header=1)

    # x_data = []
    # y_data = []
    # z_data = []

    # fig = pyplot.figure()
    # ax = Axes3D(fig)
    x1 = []
    y = []
    z = []

    # dataFile = pd.read_csv (r'C:\Users\Cassandra Olivas\ProjectACORN\testData.csv')
    # print (dataFile)

    print("NOW GENERATING HEATMAP", csvfile)
    for i, row in df.iterrows():
        x1.append(float(row.values[1]))  # x should be time. so we name it Z, in place of x
        y.append(float(row.values[2]))  # note that '2' is the column in which the iteration occurs
        # z.append(float(row.values[3]))

    plt.hist2d(x1, y, bins=30, cmap='Blues', alpha=0.7)
    cb = plt.colorbar()
    x = "Counts in Bin"
    cb.set_label(x)

    # plt.title('Data from the CSV File: X and Y Locations', color='w').set_path_effects([PathEffects.withStroke(linewidth=5, foreground='black')])
    plt.title('Data from the CSV File: X and Y Locations', color='black')

    # plt.xlabel('X Axis', color='w').set_path_effects([PathEffects.withStroke(linewidth=5, foreground='black')])
    # plt.ylabel('Y Axis', color='w').set_path_effects([PathEffects.withStroke(linewidth=5, foreground='black')])
    plt.xlabel('X Axis', color='black')
    plt.ylabel('Y Axis', color='black')

    # Use complete datetime as a unique filename
    now = str(datetime.now())
    now = now.replace(' ', '')
    now = now.replace(':', '')
    now = now.replace('.', '')  # Fully remove shit
    now = now.replace('-', '')
    print(now)
    plt.savefig('saves/' + "heat" + now + '.png', dpi=300, transparent=True)
    print("HEATMAP", csvfile, "GENERATED\n")
    # Clears the color bar upon a new plt, All axes definitions are reset
    plt.clf()
