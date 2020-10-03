import numpy as np
import cv2

img = cv2.imread('img/original.png')
mask = cv2.imread('img/mask.png',0)
mask = 255 - mask

#Image_Impainting_with_Fast Marching Method
dst = cv2.inpaint(img,mask,30,cv2.INPAINT_TELEA)

#Image_Impainting_with_Navier-Stokes
dst_NS = cv2.inpaint(img,mask,30,cv2.INPAINT_NS)

#Saving to the File
dst = cv2.cvtColor(dst,cv2.COLOR_BGR2RGB)
dst_NS = cv2.cvtColor(dst_NS,cv2.COLOR_BGR2RGB)
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

cv2.imwrite("result/input_image.jpg",img)
cv2.imwrite("result/inpaint_dst.jpg",dst)
cv2.imwrite("result/inpaint_dstNS.jpg",dst_NS)

cv2.imshow("mask",mask)
cv2.imshow('dst',dst)
cv2.imshow('dst_NS',dst_NS)
cv2.waitKey(0)
cv2.destroyAllWindows()

