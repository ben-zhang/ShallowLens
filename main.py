import cv2
import numpy as np

# We always need np with cv2, since images in opencv are np arrays.

img_path = "./images/circle.png"

img = cv2.imread(img_path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)

"""
args: image, lower bound, upper bound, Sobel kernel size, L2Gradient (bool)
The lower and upper bounds are on the intensity gradient.
Within this range, things are edgy.
"""
edgeMap = cv2.Canny(img, 100, 200)

corners = cv2.cornerHarris(gray, 2, 3, 0.04)

highlightCorners = cv2.dilate(corners, None)
img[corners>0.01*corners.max()] = [0, 0, 255]

cv2.imshow("corners", img)
cv2.waitKey(0)

# should filter out corners that aren't cornery enough