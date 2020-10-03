""" Wai Yan , 3/10/2020 """

import logging
import numpy as np
from matplotlib import pyplot as plt
import cv2
from roipoly import RoiPoly

logging.basicConfig(format='%(levelname)s ''%(processName)-10s : %(asctime)s '
                           '%(module)s.%(funcName)s:%(lineno)s %(message)s',
                    level=logging.INFO)



# Create image
input_frame = str(input("Please enter image name: "))
frame = cv2.imread(input_frame)

#Display Original Image
cv2.imshow("original_image",frame)
fig = plt.figure(dpi=100)
plt.imshow(frame)
plt.savefig("img/original.png")
plt.close(fig)

#Covert to grayscale
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
H, W = gray.shape[0] , gray.shape[1]

# # Let user draw first ROI
fig = plt.figure(dpi=100)
plt.imshow(gray, interpolation='nearest', cmap="Greys")
plt.title("left click: line segment right click or double click: close region")
plt.show(block=False)
roi1 = RoiPoly(color='r', fig=fig)

# Show the image with the first ROI
fig = plt.figure(dpi=100)
plt.imshow(gray, interpolation='nearest', cmap="Greys")
plt.colorbar()
roi1.display_roi()
plt.title('draw second ROI')
plt.show(block=False)

# # Let user draw second ROI
roi2 = RoiPoly(color='b', fig=fig)
# Show the image with both ROIs and their mean values
plt.imshow(gray, interpolation='nearest', cmap="Greys")
plt.colorbar()
for roi in [roi1, roi2]:
    roi.display_roi()
    roi.display_mean(gray)
plt.title('The two ROIs')
plt.show()

# Show ROI masks
fig = plt.figure(dpi=100)
plt.imshow(roi1.get_mask(gray) + roi2.get_mask(gray),
           interpolation='nearest', cmap="Greys")
           
plt.savefig("img/mask.png")
plt.title('ROI masks of the two ROIs')
plt.show()