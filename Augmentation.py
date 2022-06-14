# -*- coding: utf-8 -*-
"""
Created on Wed Jun 8 2022
Code to load and augment 2nd set of grapefruit peel reflectance images (and 
cross-correlation filter images) from Ecoli Test 5_6_22.  Each class needs its 
own folder.

@author: qfrederick
"""
# Libraries

#import numpy as np
import os, os.path
import datetime
from PIL import Image
from numpy import asarray
from skimage.color import rgb2hsv
#import matplotlib.pyplot as plt
import Augmentor

#%% Load Images
# folder = "C:/Users/qfrederick/Documents/Work_Code_(python)/Ecoli_Strength_UV_Set_2"
# cbs_image_list = []
# cbs_path = folder+"/Black Spot"
# valid_images = [".jpg",".gif",".png"]
# for f in os.listdir(cbs_path):
#     ext = os.path.splitext(f)[1]
#     if ext.lower() not in valid_images:
#         continue
#     cbs_image_list.append(rgb2hsv(asarray(Image.open(os.path.join(cbs_path+"/"+f)))))

#%% Augment Originals
print('Began augmenting original data at: ' + str(datetime.datetime.now().time()))
data_folder = "C:/Users/qfrederick/Documents/Work_Code_(python)/Ecoli_Strength_UV_Set_2/Just_Data"
# Using a file location on my desktop, I found it easier to copy the 7 output folders from here to a onedrive folder which can be shared.
for classes in os.listdir(data_folder):
    #pipeline
    keystone = Augmentor.Pipeline(data_folder+"/"+classes)
    
    #add ops to pipeline...pick probabilities
    keystone.rotate(probability=0.75, max_left_rotation=20, max_right_rotation=20)
    keystone.flip_left_right(probability=0.3)
    keystone.flip_top_bottom(probability=0.3)
#    keystone.random_distortion(probability=0.15, grid_width = 16, grid_height = 16, magnitude = 2)
#    keystone.zoom(probability=0.25, min_factor=1.1, max_factor=1.4)
    
    #generate some samples!...500 per class.  still should have them labeled by this point...
    keystone.sample(500)

print('Completed at: ' + str(datetime.datetime.now().time()))

#%% Augment cross-correlation Images
print('Began augmenting ccIms at: ' + str(datetime.datetime.now().time()))
data_folder = "C:/Users/qfrederick/Documents/Work_Code_(python)/Ecoli_Strength_UV_Set_2/ccIms"

for classes in os.listdir(data_folder):
    #pipeline
    keystone = Augmentor.Pipeline(data_folder+"/"+classes)
    
    #add ops to pipeline...pick probabilities
    keystone.rotate(probability=0.75, max_left_rotation=25, max_right_rotation=25)
    keystone.flip_left_right(probability=0.3)
    keystone.flip_top_bottom(probability=0.3)
#    keystone.random_distortion(probability=0.15, grid_width = 16, grid_height = 16, magnitude = 2)
#    keystone.zoom(probability=0.25, min_factor=1.1, max_factor=1.4)
    
    #generate some samples!...500 per class.  still should have them labeled by this point...
    keystone.sample(500)

print('Completed at: ' + str(datetime.datetime.now().time()))
#%% Save as np files for easier handling?

# nope, keep as directory.

#%% Load augmented dataset



