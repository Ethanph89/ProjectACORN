# Project A.C.O.R.N
https://github.com/Ethanph89/ProjectACORN

Project ACORN (Analyzing Complex Organic Rhythm in Nature)

It's a catchy name so we ran away with it. 

## About Project Acorn <img src="https://github.com/Ethanph89/ProjectACORN/blob/master/assets/acorn_main.png" width="50" height="50">
Quantify animal behavior by tracking animal movement and time spent at select variables.

## Background
The California ground squirrel (CGS) is a native Californian species ranging from Baja California to Washington. 
Considered to be one of California’s worst agricultural pest due to crop-raiding and its burrow systems undermining infrastructure (Baldwin et al. 2014). 
Since 2015, population geneticist Dr. Jennifer Cooper has been studying CGS. This has included analysis on kinship, natal dispersal, parasitism, agricultural proximity, and gut microbiomes. 

Attempt to address the following issues:
* Large quantity of videos.
* Quantifying location.
* Provide diagnostic tools. 

## Proposed Solution
A.C.O.R.N. is a Python-based software application that parses videos and obtains imaging at select intervals. The data is processed and curated data visuals are presented.

## What to Expect
This software will take user input by allowing for the input of an .mp4 file to be processed by the AWS Rekognition API (Amazon Web Service), where the video is parse into a frame per second for the entirety of the video. Once parsed, data will be collected and saved in a .csv file. The .csv file will be sent to two python scripts, respectively, turning the raw data into a timeline in the form of a scatterplot and a heatmap. Data visualization is key for this project, and so the software will display saved images after plot generation has completed.  

## Files
main.py- Instatiates the GUI with the buttons to call functions from the other class files

sqHandlieVideo.py- Asks user for video and iterates through each frame of the video for data

sqVideo.py- Splits the video into images and sends the images to AWS Rekognition for analysis

sqHeatmap.py- Generates the heatmap graph type

sqTimeline.py- Generates the timeline graph type

test.py- Unit tests for each function

## Run Process
1. Download the source code

2. Install all prerequisite libraries with 'pip install' command (see libraries section below)

3. Setup AWSCLI using AWS Root user account

4. Run main.py

5. Upload a .mp4 file with squirrel footage or upload a CSV with existing data (testdata.csv in repository is usable for testing)

6. Select desired graph type and click generate graph

(Note: Executable file coming in future update)

## Early Renders
<img src="https://github.com/Ethanph89/ProjectACORN/blob/featureTimeline/assets/data.png" width="350" height="200">
<img src="https://github.com/Ethanph89/ProjectACORN/tree/master/assets/heatmap.png" width="350" height="200">

## Interpreter
* Python 3.8

## Libraries
* PIL/Pillow 7.1.1
* awscli 1.18.36
* boto3 1.12.36
* matplotlib 3.2.1
* numpy 1.18.3
* pandas 1.0.3

## [Amazon Rekognition](https://aws.amazon.com/rekognition/)
* AWS Account with working credentials
* Configured AWS CLI settings
 
## Authors
* **Andrew Bhatti, Giancarlo Garcia Deleon, Ethan Hunt, Cassandra Olivas**
