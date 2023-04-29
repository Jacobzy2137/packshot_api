import cv2
import os
import urllib.request
import numpy as np
from PIL import Image
from io import BytesIO
from fastapi import FastAPI


def find_white_background(imgpath, threshold=0.45):
    img_array = cv2.imread(imgpath)
    background = np.array([255, 255, 255])
    percent = (img_array == background).sum() / img_array.size
    if percent >= threshold:
        print(percent)
        return True
    else:
        return False

img_path = 'image.jpg'
packshot_check = find_white_background(img_path)



if packshot_check == True:
    print('Ten obrazek to PACKSHOT')
else:
    print('ten obrazek NIE JEST PACKSHOTEM')

if os.path.exists(img_path):
    os.remove(img_path)