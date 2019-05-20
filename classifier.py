import cv2
from cv2.ximgproc import createSuperpixelSLIC
from cv2.ximgproc import SLIC as SLIC_CONST
import numpy as np

# We always need np with cv2, since images in opencv are np arrays.

def pre_process(img):
    region_size = 100 # average superpixel size
    ruler = 15

    # SLIC clusters on values (L, A, B, X, Y)
    img_lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

    slic = createSuperpixelSLIC(img_lab, SLIC_CONST, region_size, ruler)



    slic.iterate(10)

    superpixels = slic.getLabelContourMask(True)
    cv2.imshow("img", superpixels)
    cv2.waitKey(0)