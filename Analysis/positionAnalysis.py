from read import screenshot
import cv2
def detectSquare():
    img = screenshot.screenshot()
    contours, _ = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours: 
  
    # here we are ignoring first counter because  
    # findcontour function detects whole image as shape 
        i = 0
        if i == 0: 
            i = 1
            continue
    
        # cv2.approxPloyDP() function to approximate the shape 
        approx = cv2.approxPolyDP( 
            contour, 0.01 * cv2.arcLength(contour, True), True) 
        
        # using drawContours() function 
        cv2.drawContours(img, [contour], 0, (0, 0, 255), 5) 
    
        # finding center point of shape 
        M = cv2.moments(contour) 
        if M['m00'] != 0.0: 
            x = int(M['m10']/M['m00']) 
            y = int(M['m01']/M['m00']) 
    
        # putting shape name at center of each shape 
        if len(approx) == 3: 
            cv2.putText(img, 'Triangle', (x, y), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2) 
    
        elif len(approx) == 4: 
            cv2.putText(img, 'Quadrilateral', (x, y), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2) 
    
        elif len(approx) == 5: 
            cv2.putText(img, 'Pentagon', (x, y), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2) 
    
        elif len(approx) == 6: 
            cv2.putText(img, 'Hexagon', (x, y), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2) 
    
        else: 
            cv2.putText(img, 'circle', (x, y), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2) 
    
    # displaying the image after drawing contours 
    cv2.imshow('shapes', img) 
  
cv2.waitKey(0) 
cv2.destroyAllWindows() 