"""
author: cray-sh
date: 2023.01.23

This file is the starting place for the first problem
Problem 1 has a lot to do with manipulating images and/or formating them
"""
#%% Example 1 from Module

#from PIL import Image
#im = Image.open(<file_here>)
#new_im = im.resize((640,480))
#new_im.save("example_resized.jpg")

#%% Example 2 from Module
#We can also use typical dot notation antics to chain commands

#from PIL import Image
#im = Image.open(<file_here>)
#im.rotate(180).resize((640,480)).save("flipped_and_resized.jpg")

#%% Block 1: One image Case: Will need to perform 4 operations; rotate(90), resize((128,128)), format change to .jpg, and save

from PIL import Image as Im
import os
import sys

new_path = 'C:\\Users\\ADP55\\Desktop\\Master Scripts\\Python-Cert-Final-Problems\\problem 1\\New location\\'


#opens image at file location
image0 = Im.open('sea_damn.png')

#resizes the image opened
image1 = image0.resize((192,192))

#rotates the image by 90 degrees
image2 = image1.rotate(90)

#formats from current format to .jpg

image2_rgb = image2.convert('RGB')
image2_rgb.save(new_path + 'sea_damn.jpeg')

#The above block 1 works to convert a single file that is given, manipulates as wanted, and then saves it under the jpeg format
#The inbetween convert step is placed just incase an image in RGBA is opened, as RGBA cannot be directly converted to jpeg without ditching the A
