import numpy as np
from PIL import Image
import face_recognition
import cv2
import shutil
import os, glob
import imagehash

'''Script name is self explanatory'''

def similarity_score(x, y):
    # similarity score in 4-d space
    dist = np.linalg.norm(x-y)
    return dist


def calculateDistance(image1, image2):
    return np.sqrt(np.sum((image1-image2)**2))


def hash_sim(path1, path2):

    img_1 = Image.open(path1)
    img_2 = Image.open(path2)
    hash1 = imagehash.average_hash(img_1)
    hash2 = imagehash.average_hash(img_2)
    diff = hash1 - hash2
    return diff


def path_to_val(path):
    pass