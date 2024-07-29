import cv2
import numpy as np
image_path=r"C:\Users\DARSHAN M\OneDrive\Portfolio\Pictures\dunkirk.png"
img=cv2.imread(image_path)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh=cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
contours, hierarchy=cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
contour_image=img.copy()
cv2.drawContours(contour_image,contours,-1,(0,255,0),2)
cv2.imshow("Original Image",img)
cv2.imshow('Contours',contour_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
