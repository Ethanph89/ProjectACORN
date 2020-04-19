import glob
import pandas as pd # Import CSV
import random
import matplotlib.pyplot as plt
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D

# Use this function to check if the input file has the correct extension.
# def filebrowser(ext=""):
#     "Returns files with an extension"
#     return [f for f in glob.glob(f"*{ext}")]
# x = filebrowser(".csv")

#Interchangeably, we can have user input, but we're not usign console, so no need for it now, simply replace the value for filename.
filename = "data.csv"

df = pd.read_csv(filename, delimiter=',', header=1) # Read in csv and save as df. 
fig = pyplot.figure() # Init plot
ax = Axes3D(fig)
x=[]
y=[]
z=[]
newelem = filename[:-4]

for i, row in df.iterrows():
    x.append(float(row.values[1])) #x should be time. so we name it Z, in place of x
    y.append(float(row.values[2])) # note that '2' is the column in which the iteration occurs
    z.append(float(row.values[3]))
    
ax.scatter(z,x,y, '-o')
ax.set_zlabel('Z Coordinates')
ax.set_ylabel('Y Coordinates')
ax.set_xlabel('TIME(X)')
ax.plot(z,x,y, color='r', lw=1) # lw is line width
# pyplot.show() # Scatterplot using CSV (MAIN) Dataframe 1
fig.savefig('saves/'+ newelem + '.png', dpi=1000, bbox_inches = 'tight')
