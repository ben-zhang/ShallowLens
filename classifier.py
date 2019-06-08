import cv2
from cv2.ximgproc import createSuperpixelSLIC
from cv2.ximgproc import SLIC as SLIC_CONST
from skimage.segmentation import slic
import numpy as np

# We always need np with cv2, since images in opencv are np arrays.

def pre_process(img):
    region_size = 100 # average superpixel size
    ruler = 15

    # SLIC clusters on values (L, A, B, X, Y)
    img_lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

    # Cluster and extract cluster centers
    superpixels = slic()