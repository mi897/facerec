import numpy as np
import face_recognition
import cv2
import os, glob
import helpers

'''Script compares the similarity between images'''

# main folder which has all folders 
path_main = "all_faces"

# read images from two folders
fn1 = 1
fn2 = 2

paths_to_images_1= os.listdir("{}/{}".format(path_main, fn1))[0]
paths_to_images_2= os.listdir("{}/{}".format(path_main, fn2))[0]

img_path1 = "{}/{}/{}". format(path_main, fn1, paths_to_images_1)
img_path2 = "{}/{}/{}". format(path_main, fn2, paths_to_images_2)

print(img_path1, img_path2)

#p1 = "t.jpg"
#p2 = "s.jpg"
#score = helpers.face_comp(p1, p2)
#print(score)

sim = helpers.similarity_score(img_path1, img_path2)
print(sim)

# sim in 50 to 100 - same face
# sim > 100 - diff face
