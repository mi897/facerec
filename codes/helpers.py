import numpy as np
from PIL import Image
import face_recognition
import cv2
import shutil
import os, glob
import imagehash

'''Script name is self explanatory'''

def similarity_score(img_path1, img_path2):

    loc1 = []
    loc2 = []
    
    loc1.append(path_to_val(img_path1))
    loc2.append(path_to_val(img_path2))

    loc1 = np.array(loc1[0], dtype="int")
    loc2 = np.array(loc2[0], dtype="int")

    # similarity score in 4-d space
    dist = np.linalg.norm(loc1 - loc2)
    # got 99.9 for similar faces in two frames

    return dist


def mse(image_path_1, image_path_2):
    image1 = cv2.resize(cv2.imread(image_path_1), (120,120))
    image2 = cv2.resize(cv2.imread(image_path_2), (120,120))
    
    err = np.sum((image1.astype("float") - image2.astype("float")) ** 2)
    err /= float(image1.shape[0] * image1.shape[1])

    # return the MSE, the lower the error, the more "similar"
    return err


def eucl_dist(image_path_1, image_path_2):

    image1 = cv2.resize(cv2.imread(image_path_1), (120,120))
    image2 = cv2.resize(cv2.imread(image_path_2), (120,120))

    dist = np.sqrt(np.sum((image1-image2)**2))
    return dist


def hash_sim(path1, path2):
    
    assert type(path1) is str, "I need a string"
    assert type(path2) is str, "I need a string"

    img_1 = Image.open(path1)
    img_2 = Image.open(path2)
    hash1 = imagehash.average_hash(img_1)
    hash2 = imagehash.average_hash(img_2)
    diff = hash1 - hash2
    
    return diff

def face_comp(p1, p2):

    assert type(p1) is str, "I need a string"
    assert type(p2) is str, "I need a string"

    known_image = face_recognition.load_image_file(p1)
    unknown_image = face_recognition.load_image_file(p2)

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
    return results


def path_to_val(path):
    '''
    Input: an image path such as -> all_faces/1/163_318_271_426.jpg
    Output: top = 163, right = 318, left = 271, bottom = 426        
    '''
    #import pdb; pdb.set_trace()
    loc = path[-19:]
    top = loc[:3]
    right = loc[4:7]
    left = loc[8:11]
    bottom = loc[12:15]

    return top, right, left, bottom


def get_image_paths(folder, path_main):
    '''
    Input: folder - folder number
            path_main - name of main directory inside which the folder resides
    
    Returns: all paths of images  
    '''
    
    assert type(folder) is int, "I need integers"
    assert type(path_main) is str, "I need strings"

    paths_to_images = [path for path in os.listdir("{}/{}".format(path_main, folder))]
    count = len(paths_to_images)
    img_paths = []

    for i in range(count): 
        img_paths.append("{}/{}/{}". format(path_main, folder, paths_to_images[i]))
    
    return img_paths


# Helper function to extract the number from the filename
def get_number(filename):
    return int(filename[:filename.find('.')])

# Sort the array paths using the number returned by the function get_number
def sort_paths(paths):
    paths.sort(key = get_number)
    return paths