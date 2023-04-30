import cv2
import os
import requests
import urllib.request
import numpy as np
from PIL import Image
from fastapi import FastAPI


app = FastAPI()
@app.get('/{url}')
async def root():
    img_path = 'image.jpg'
    urllib.request.urlretrieve(url, img_path)
    threshold = 0.35
    img_array = cv2.imread(imgpath)
    background = np.array([255, 255, 255])
    percent = (img_array == background).sum() / img_array.size
    if percent >= threshold:
        x = {'packshot': 'obraz to packshot'}
    else:
        x = {'packshot': 'obraz nie jest packshotem'}

    if os.path.exists(img_path):
      os.remove(img_path)

    return x
