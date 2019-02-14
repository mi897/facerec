from PIL import Image
import face_recognition
import cv2
import shutil
import os, glob

'''
- Get all image paths inside the image sequence directory - done
- For each image in all image
    * Load image - done
    * Make a folder named as image number - done
    * Detect face in image - done
    * Crop face from image - done
    * Rename face as x,y pos - done
    * Save image in folder

- Ouptut 
    * Number of folders as number of images
    * A folder has number of faces detected from the image
'''
# https://www.thepythoncorner.com/2018/04/how-to-make-your-code-faster-by-using-a-cache-in-python/?doing_wp_cron=1550052809.3500170707702636718750


# read all paths in directory
paths_to_images= os.listdir("frames")

# main folder which has all folders 
path_main = "all_faces"

shutil.rmtree(path_main)
# make new folder
os.makedirs(path_main)


folder_count = 0
for path in paths_to_images[:10]:
    # load image
    img = cv2.imread("frames/{}". format(path))
    #dummy = cv2.imread("frames/0.jpg")
    os.makedirs("{}/{}".format(path_main, folder_count))
    # get faces locations
    face_locations = face_recognition.face_locations(img)

    count = 0
    for face_location in face_locations:

        top, right, bottom, left = face_location
        # crop image of face
        face_image = img[top:bottom, left:right]

        # images saved as top, left, bottom, right as their names
        cv2.imwrite("{}/{}/{}_{}_{}_{}.jpg" .format(path_main, folder_count, top, left, bottom, right), face_image)
        count+=1

    print("Got and saved {} faces in folder {}" .format(count, folder_count))
    folder_count+=1

cv2.destroyAllWindows()
