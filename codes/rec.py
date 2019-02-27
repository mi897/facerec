from PIL import Image
import face_recognition
import cv2
import shutil
import os
import matplotlib.pyplot as plt

'''
Scirpt reads the image and finds faces in image and then returns the location
where the face is detected.
'''

def detect_and_extract():
    count = 0
    for face_location in face_locations:

        top, right, bottom, left = face_location
        #print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))
        #face_image = image[top:bottom, left:right]
        #cv2.imwrite("faces/face{}.jpg" .format(count), face_image)
        count+=1
    print("Done!")
    #cv2.destroyAllWindows()

def plot_img(image):
    # For testing
    cv2.rectangle(image, (498, 766), (290, 557), (0,255,0), 5)
    cv2.imshow("show", image)
    plt.imshow(image)
    plt.show()


#path_frames = "faces"
#shutil.rmtree(path_frames)
#os.makedirs(path_frames)

number = 49
image = face_recognition.load_image_file("frames/{}.jpg".format(number))
face_locations = face_recognition.face_locations(image)

print("I found {} face(s) in this photograph.".format(len(face_locations)))
detect_and_extract()

# for testing only
#plot_img(image)