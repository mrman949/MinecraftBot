import numpy as np
import cv2
from mss import mss
from PIL import Image

mon = {'left': 0, 'top': 0, 'width': 3840, 'height': 2160}

def screenshot():
    with mss() as sct:
            screenShot = sct.grab(mon)
            img = Image.frombytes(
                'RGB', 
                (screenShot.width, screenShot.height), 
                screenShot.rgb, 
            )
            cv2.destroyAllWindows()
    return img
