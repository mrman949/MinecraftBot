import numpy as np
import cv2
from mss import mss
from PIL import Image
import os
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
    return np.array(img)

#Takes an image like the one supplied by screenshot
def storeshot(img):
    currentDirectory = r'Analysis\storedImages'
    print(os.listdir(currentDirectory))
    latest = int((os.listdir(currentDirectory)[-1]).removesuffix('.jpg'))
    name = latest + 1
    cv2.imwrite(currentDirectory + "/" + str(name) + ".jpg", img)


