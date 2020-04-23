# AUTHOR:
# Cassandra Olivas
# IMPORTS---------------------------------------------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
style.use('ggplot')

# CLASS DEFINITIONS-----------------------------------------------------------------------------------------------------



# BODY FUNCTIONS--------------------------------------------------------------------------------------------------------

def generateHeatmap():
    x_data = []
    y_data = []
    z_data = []

    # dataFile = pd.read_csv (r'C:\Users\Cassandra Olivas\ProjectACORN\testData.csv')
    # print (dataFile)

    x_data, y_data, z_data = np.loadtxt('testData.txt',
                                        unpack=True,
                                        delimiter='\t')

    plt.hist2d(x_data, y_data, bins=30, cmap='Blues')
    cb = plt.colorbar()
    cb.set_label('counts in bin')

    plt.title('Data from the CSV File: X and Y Locations')

    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')