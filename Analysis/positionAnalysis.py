import readScreen
import cv2
import matplotlib.pyplot as plt
import numpy as np
import time
import cache
import os
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

def detectImageMultiScale(img1, img2, name ,scale_start=0.4, scale_end=1.3, scale_step=0.1, threshold=0.81):
    # Convert img1 to grayscale
    #img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

    found = 0  # Counter to track matches

    # Loop over scales from scale_start to scale_end
    for scale in np.arange(scale_start, scale_end, scale_step):
        # Create a fresh copy of the original img1 for each scale iteration
        img_copy = img1.copy()

        # Resize img2 (the template) according to the current scale
        #print(img2.shape, img2.shape[1])
        cropped = img2[10:110, 10:110]
        cv2.imshow("",cropped)
        cv2.waitKey(10)
        img2r = cropped
        
        scaled_img2 = cv2.resize(img2r, (int(img2r.shape[1] * scale), int(img2r.shape[0] * scale)))

        # If the scaled template size is larger than img1, skip this iteration
        if scaled_img2.shape[0] > img1_gray.shape[0] or scaled_img2.shape[1] > img1_gray.shape[1]:
            continue
#TM_CCOEFF_NORMED
        # Apply template matching
        result = cv2.matchTemplate(img1_gray, scaled_img2, cv2.TM_CCOEFF_NORMED)
        
        # Find all locations with match confidence above the threshold
        match_locations = np.where(result >= threshold)
        
        h, w = scaled_img2.shape

        # Draw rectangles for all matches
        for (y, x) in zip(match_locations[0], match_locations[1]):
            top_left = (x, y)
            bottom_right = (top_left[0] + w, top_left[1] + h)
            cv2.rectangle(img_copy, top_left, bottom_right, (255, 255, 255), 2)
            found += 1

        # Show the image for this scale with the current matches
        if len(match_locations[0]) > 0:
            print(f"Matches found at scale {scale:.2f}: {len(match_locations[0])} match(es).", name)
            img1_resized = cv2.resize(img_copy, (1920, 1080))
            cv2.imshow(f"Detected Icon(s) at scale {scale:.2f}", img1_resized)
            cv2.waitKey(8000)
            cv2.destroyAllWindows()
            time.sleep(1)

    if found == 0:
        print(name)
        pass
        #print("No matches found.")

# Test the function



# Call the function
champnames = os.listdir("Analysis/trainingImages")
#print(champnames)
for x in champnames:
    iconName = x
    Screen = np.array(readScreen.screenshotRAW())
    #iconName = 'malphite'
    icon = cv2.imread('C:/Users/Trevor/Desktop/Bots/Analysis/trainingImages/'+iconName, cv2.IMREAD_GRAYSCALE)
    detectImageMultiScale(Screen, icon, x)