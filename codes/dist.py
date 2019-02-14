import numpy as np
import face_recognition
import cv2
import os, glob
from PIL import Image
import imagehash

'''Script compares the similarity between images'''

def compare_faces(p1, p2):
    pass

a = np.array((110, 253, 239, 382))
b = np.array((163, 318, 271, 426))
#import pdb; pdb.set_trace()

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

known_image = face_recognition.load_image_file(img_path1)
unknown_image = face_recognition.load_image_file(img_path2)
print(known_image.shape)

known_encoding = face_recognition.face_encodings(known_image)
if len(known_encoding) > 0:
    known_encoding = known_encoding[0]
else:
    print("No faces found while known_encoding!")

unknown_encoding = face_recognition.face_encodings(unknown_image)

if len(unknown_encoding) > 0:
    unknown_encoding = unknown_encoding[0]
else:
    print("No faces found while unknown_encoding!")

results = face_recognition.compare_faces([known_encoding], unknown_encoding)
print(results)