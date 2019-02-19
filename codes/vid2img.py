import cv2
import numpy as np
import shutil
import imutils
import os

'''Script take in a video and saves each frame as an image as a sequence.
'''

cap = cv2.VideoCapture('vid2.MOV')
count = 0

path_frames = "frames"
shutil.rmtree(path_frames)
os.makedirs(path_frames)

if (cap.isOpened()== False): 
  print("Error opening video stream or file")
 
while(cap.isOpened()):
  
  ret, frame = cap.read()
  if ret == True:
    #frame = cv2.resize(frame, (600, 400))
    frame = imutils.rotate(frame, -180)
    cv2.imshow('Frame',frame)
    cv2.imwrite("frames/{}.jpg" .format(count), frame)
    count+=1

    if cv2.waitKey(10) & 0xFF == ord('q'):
      break
 
  else: 
    break

cap.release()
cv2.destroyAllWindows()
