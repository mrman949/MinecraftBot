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
            #cv2.destroyAllWindows()
    return np.array(img)

def screenshotRAW():
     currentDirectory = r'Analysis\storedImages'
     with mss() as sct:
        screenShot = sct.grab(mon)
        if os.listdir(currentDirectory) != []:
            latest = int((os.listdir(currentDirectory)[-1]).removesuffix('.jpg'))
        else:
            latest = - 1
        name = latest + 1

        img = Image.frombytes(
                'RGB', 
                (screenShot.width, screenShot.height), 
                screenShot.rgb, 
            )
        
        #cv2.imwrite(currentDirectory + "/" + str(name) + ".jpg", np.array(img))
        return img


#Takes an image like the one supplied by screenshot
def storeshot(img):
    currentDirectory = r'Analysis\storedImages'

    if os.listdir(currentDirectory) != []:
        latest = int((os.listdir(currentDirectory)[-1]).removesuffix('.jpg'))
    else:
         latest = - 1
    name = latest + 1
    cv2.imwrite(currentDirectory + "/" + str(name) + ".jpg", img)

