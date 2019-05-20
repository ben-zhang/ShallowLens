import cv2
import numpy as np
import classifier

# We run the classifier from here.

img_path = "./images/ouchmouse.jpg"
img_circle_path = "./images/circle.png"

img = cv2.imread(img_circle_path)

classifier.pre_process(img)