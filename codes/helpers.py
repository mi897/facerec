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
    
    assert type(p1) is str, "I need a string"
    assert type(p2) is str, "I need a string"

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
    pass