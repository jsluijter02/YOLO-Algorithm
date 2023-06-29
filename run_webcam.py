import cv2
import numpy as np 
#get the model to overwrite the bound boxes

capture = cv2.VideoCapture(0)

#we need to be able to open the camera
if not capture.isOpened():
    raise IOError("Webcam closed")

while True:
    ret, frame = capture.read()
    cv2.resize(frame, (488,488)) #resize it to the pixel width and height yolo demands
    #TODO make sure the yolo algo does its predictions and outputs bounding boxes
    cv2.imshow("Yolo-Detection", frame)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break 

capture.release()
cv2.destroyAllWindows()


