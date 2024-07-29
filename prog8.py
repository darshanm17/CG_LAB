import cv2
import numpy as np
image_path=r'C:\Users\DARSHAN M\OneDrive\Portfolio\Pictures\dunkirk.png'
img=cv2.imread(image_path)
height,width,_=img.shape
rm=cv2.getRotationMatrix2D((width/2,height/2),45,1)
sm=np.float32([[1.5,0,0],[0,1.5,0]])
tm=np.float32([[1,0,100],[0,1,50]])
r=cv2.warpAffine(img,rm,(width,height))
s=cv2.warpAffine(img,sm,(int(width*1.5),int(height*1.5)))
t=cv2.warpAffine(img,tm,(width,height))
cv2.imshow("original Image",img)
cv2.imshow("Rotated Image",r)
cv2.imshow("Scaled Image",s)
cv2.imshow("Translated Image",t)
cv2.waitKey(0)
cv2.destroyAllWindows()