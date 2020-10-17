#import dependencies 
import numpy as np
import pandas as pd
import os


#  load the testing result into dataframe
detectionResult = pd.read_csv("../Data/Source_Images/Test_Image_Detection_Results/Detection_Results.csv") 


#  Export each row into input directory
for ind in detectionResult.index: 
     filename = 'mAP/input/detection-results/' + os.path.splitext(detectionResult['image'][ind])[0] + '.txt'
     with open(filename, 'a') as f1:
          predictionStr = 'Gun' + ' ' + str(detectionResult['confidence'][ind]) + ' ' + str(detectionResult['xmin'][ind]) + ' ' +  str(detectionResult['ymin'][ind]) + ' ' + str(detectionResult['xmax'][ind]) + ' ' + str(detectionResult['ymax'][ind]) + '\n'
          f1.write(predictionStr)


# Load the testing image annotation file into dataframe
testDataFrame = pd.read_csv("../Data/Source_Images/Test_Images/TestingSetGunImage-export.csv")


# Export each row into ground truth input direcotry
for ind in testDataFrame.index: 
     filename = 'mAP/input/ground-truth/' + os.path.splitext(testDataFrame['image'][ind])[0] + '.txt'
     with open(filename, 'a') as f1:
          testingStr = testDataFrame['label'][ind] + ' ' + str(testDataFrame['xmin'][ind]) + ' ' +  str(testDataFrame['ymin'][ind]) + ' ' + str(testDataFrame['xmax'][ind]) + ' ' + str(testDataFrame['ymax'][ind]) + '\n'
          f1.write(testingStr)





