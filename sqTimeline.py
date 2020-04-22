# IMPORTS---------------------------------------------------------------------------------------------------------------
import glob
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd


# CLASS DEFINITIONS-----------------------------------------------------------------------------------------------------



# BODY FUNCTIONS--------------------------------------------------------------------------------------------------------
def generateTimeline():
    #os.chdir("Desktop/Python Scripts/") #Note: this directory will be changed at the very end to endure that it is in the programs local directory.
    #currdir = os.getcwd()
    #print(currdir)

    #final_directory = os.path.join(currdir, r'new_folder')
    #if not os.path.exists("saves"):
    #    os.makedirs("saves")
    #    print("Created new directory for new scatterplots.")
    #else:
    #    print("Directory to save new scatterplots already exists.\n")

    print("NOW GENERATING SCATTERPLOTS")

    x = filebrowser('.csv')

    for elem in x:
        df = pd.read_csv(elem, delimiter=',', header=1)
        print("NEW CSV FILE DETECTED NAMED:", elem)

        ## all files are saved as a list.
        # Now we want to run everything in our list through our script
        # Have a nested for loop

        # sec_column = df.iloc[:, 1]
        # print(sec_column)

        fig = pyplot.figure()
        ax = Axes3D(fig)
        x = []
        y = []
        z = []

        newelem = elem[:-4]

        print("NOW GENERATING SCATTERPLOT", elem)
        for i, row in df.iterrows():
            x.append(float(row.values[1]))  # x should be time. so we name it Z, in place of x
            y.append(float(row.values[2]))  # note that '2' is the column in which the iteration occurs
            z.append(float(row.values[3]))

        ax.scatter(z, x, y, '-o')

        ax.set_zlabel('Z Coordinates')
        ax.set_ylabel('Y Coordinates')
        ax.set_xlabel('TIME(X)')
        ax.plot(z, x, y, color='r', lw=1)  # lw is line width
        #     pyplot.show() # Scatterplot using CSV (MAIN) Dataframe 1
        fig.savefig('saves/' + newelem + '.png', dpi=1000, bbox_inches='tight')
        print("SCATTERPLOT", elem, "GENERATED\n")

# find the CSVs in a folder to generate
def filebrowser(ext=""):
    # Returns files with an extension
    return [f for f in glob.glob(f"*{ext}")]
