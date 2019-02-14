from PIL import Image
import face_recognition
import cv2
import shutil
import os

path_frames = "faces"
shutil.rmtree(path_frames)
os.makedirs(path_frames)

image = face_recognition.load_image_file("test.jpg")
face_locations = face_recognition.face_locations(image)

print("I found {} face(s) in this photograph.".format(len(face_locations)))

count = 0
for face_location in face_locations:

    top, right, bottom, left = face_location
    print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

    face_image = image[top:bottom, left:right]
    #cv2.imwrite("faces/face{}.jpg" .format(count), face_image)
    count+=1

cv2.destroyAllWindows()
