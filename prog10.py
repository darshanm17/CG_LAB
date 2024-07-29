import cv2
import numpy as np
image_path=r"C:\Users\DARSHAN M\OneDrive\Portfolio\Pictures\dunkirk.png"
img=cv2.imread(image_path)
gb=cv2.GaussianBlur(img,(5,5),0)
mb=cv2.medianBlur(img,5)
bf=cv2.bilateralFilter(img,9,75,75)
cv2.imshow("Original Image",img)
cv2.imshow("Gaussian Blur Image",gb)
cv2.imshow("Median Blur Image",mb)
cv2.imshow("Bilateral Filter Image",bf)
cv2.waitKey(0)
cv2.destroyAllWindows()