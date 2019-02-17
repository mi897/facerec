import numpy as np
import face_recognition
import cv2
import os, glob
import helpers

'''Script compares the similarity between images'''

# main folder which has all folders 
path_main = "all_faces"

# read images from two folders
paths_to_images_1= os.listdir("{}/0".format(path_main))[0]
paths_to_images_2= os.listdir("{}/1".format(path_main))[0]

img_path1 = "{}/0/{}". format(path_main, paths_to_images_1)
img_path2 = "{}/1/{}". format(path_main, paths_to_images_2)

p1 = "2.jpg"
p2 = "s.jpg"

#(t, r, l, b) = helpers.path_to_val(img_path1)

score = helpers.face_comp(p1, p2)
print(score)
