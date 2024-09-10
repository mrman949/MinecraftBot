import readScreen
import cv2
import matplotlib.pyplot as plt
import numpy as np
def detectSquare():
    img = readScreen.screenshot()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
  
# setting threshold of gray image 
    _, threshold = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY) 
    contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    i = 0
    for contour in contours: 
  
    # here we are ignoring first counter because  
    # findcontour function detects whole image as shape 
        
        if i == 0: 
            i = 1
            continue
    
        # cv2.approxPloyDP() function to approximate the shape 
        approx = cv2.approxPolyDP( 
            contour, 0.01 * cv2.arcLength(contour, True), True) 
        
        # using drawContours() function 
        cv2.drawContours(img, [contour], 0, (0, 0, 255), 1) 
    
        # finding center point of shape 
        M = cv2.moments(contour) 
        if M['m00'] != 0.0: 
            x = int(M['m10']/M['m00']) 
            y = int(M['m01']/M['m00']) 
    
        # putting shape name at center of each shape 
        if len(approx) == 4: 
            cv2.putText(img, 'Quadrilateral', (x, y), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.2, (255, 255, 255), 1) 
        else: 
            cv2.putText(img, 'circle', (x, y), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.2, (255, 255, 255), 1) 
    # displaying the image after drawing contours 
    cv2.imshow('shapes', img) 
  
    cv2.waitKey(0) 
    cv2.destroyAllWindows() 

def detectImage(img1, img2):
    # Convert both images to grayscale (if not already)
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

    # Ensure img2 (the icon) is smaller than img1 (the desktop screenshot)
    if img2.shape[0] > img1.shape[0] or img2.shape[1] > img1.shape[1]:
        print("Icon is larger than the screenshot. Ensure img2 is smaller.")
        return

    # Apply template matching
    result = cv2.matchTemplate(img1, img2, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    threshold = 0.8  # Higher threshold means stricter matching

    if max_val >= threshold:
        print(f"Match found with confidence: {max_val}")

        top_left = max_loc
        h, w = img2.shape
        bottom_right = (top_left[0] + w, top_left[1] + h)
        cv2.rectangle(img1, top_left, bottom_right, (255, 255, 255), 2)
        img1_resized = cv2.resize(img1, (1920,1080))

        cv2.imshow("Detected Icon", img1_resized)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Discord icon not detected.")

# Test the function
icon = cv2.imread('C:/Users/Trevor/Desktop/Bots/Analysis/trainingImages/discordIcon.png', cv2.IMREAD_GRAYSCALE)
Screen = np.array(readScreen.screenshotRAW())

# Call the function
detectImage(Screen, icon)