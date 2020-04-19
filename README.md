# Project A.C.O.R.N
Project ACORN (Analyzing Complex Organic Rhythm in Nature)

## About Project Acorn <img src="https://github.com/Ethanph89/ProjectACORN/blob/featureTimeline/assets/acorn.png" width="75" height="50">

## Background
The California ground squirrel (CGS) is a native Californian species ranging from Baja California to Washington. 
Considered to be one of California’s worst agricultural pest due to crop-raiding and its burrow systems undermining infrastructure (Baldwin et al. 2014). 
Since 2015, population geneticist Dr. Jennifer Cooper has been studying CGS. This has included analysis on kinship, natal dispersal, parasitism, agricultural proximity, and gut microbiomes. 

## Proposed Solution
A.C.O.R.N. is a Python-based software application that parses videos and obtains imaging at select intervals. The data is processed and curated data visuals are presented.

## What to Expect
This software will take user input by allowing for the input of an .mp4 file to be processed by the AWS Rekognition API (Amazon Web Service), where the video is parse into a frame per second for the entirety of the video. Once parsed, data will be collected and saved in a .csv file. The .csv file will be sent to two python scripts, respectively, turning the raw data into a timeline in the form of a scatterplot and a heatmap. Data visualization is key for this project, and so the software will display saved images after plot generation has completed.  

## Early Renders
<img src="https://github.com/Ethanph89/ProjectACORN/blob/featureTimeline/assets/data.png">

## Authors
* **Andrew Bhatti, Giancarlo Garcia Deleon, Ethan Hunt, Cassandra Olivas**