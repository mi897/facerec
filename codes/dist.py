import numpy as np
import face_recognition
import cv2
import os, glob
import helpers

'''Script compares the similarity between images'''

def compare_faces(p1, p2):
    pass

# face locations from frame 0 and 1
a = np.array((110, 253, 239, 382))
b = np.array((163, 318, 271, 426))

# main folder which has all folders 
path_main = "all_faces"

# read images from two folders
paths_to_images_1= os.listdir("{}/0".format(path_main))[0]
paths_to_images_2= os.listdir("{}/1".format(path_main))[0]
img_path1 = "{}/0/{}". format(path_main, paths_to_images_1)
img_path2 = "{}/1/{}". format(path_main, paths_to_images_2)

# load images
#img1 = cv2.imread(img_path1)
#img2 = cv2.imread(img_path2)
#print(img1.shape, img2.shape)

p1 = "p1.jpg"
p2 = "p2.jpg"

score = helpers.face_comp(p1, p2)
print(score)
