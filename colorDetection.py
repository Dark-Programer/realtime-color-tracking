import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)
while (1):
    _, frame = cap.read() # Take each frame
    
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV) # Convert BGR to HSV
    
    # define range of blue color in HSV
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])
    
    # define range of red color in HSV
    lower_red = np.array([170, 50, 50])
    upper_red = np.array([180, 255, 255])
    
    # define range of green color in HSV
    lower_green = np.array([40, 40, 40])
    upper_green = np.array([80, 255, 255])

    # Threshold the HSV image to get only Green colors
    maskGreen = cv.inRange(hsv, lower_green, upper_green)

    # Threshold the HSV image to get only red colors
    maskRed = cv.inRange(hsv, lower_red, upper_red)

    # Threshold the HSV image to get only blue colors
    maskBlue = cv.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image and we got the color we want to detect
    resGreen = cv.bitwise_and(frame, frame, mask=maskGreen)
    resRed = cv.bitwise_and(frame, frame, mask=maskRed)
    resBlue = cv.bitwise_and(frame, frame, mask=maskBlue)

    cv.imshow('frame', frame)
    cv.imshow('Green', resGreen)
    cv.imshow('Red', resRed)
    cv.imshow('Blue', resBlue)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()
