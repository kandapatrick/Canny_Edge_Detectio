import cv2
import numpy as np

image = cv2.imread('My_Image.jpg')

# Convert to graycsale
img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Blur the image for better edge detection
img_blur = cv2.GaussianBlur(img_gray, (3,3), 0) 

# Canny Edge Detection
cv2.imshow('My Image', image)
#cv2.waitKey(0)

Canny_Edge_Image = cv2.Canny(image=img_blur, threshold1=100, threshold2=200) # Canny Edge Detection
# Display Canny Edge Detection Image
cv2.imshow('Canny Edge Detection', Canny_Edge_Image)
cv2.waitKey(0)

filename = 'Canny_Edge_Image.jpg'

cv2.imwrite(filename, Canny_Edge_Image)
cv2.destroyAllWindows()

