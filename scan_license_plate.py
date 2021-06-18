import cv2
import numpy as np

# Image to be analyzed
img = cv2.imread('images/license plate.jpg')

# Image treatment
img_reshaped = cv2.resize(img, (640, 360))

# Shape of the new image (license plate)
width, height = 400, 150

# Points in the image to be cropped
pts1 = np.float32([[2761, 1386], [2964, 1369], [2766, 1479], [2975, 1457]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

# Creation of new image
matrix = cv2.getPerspectiveTransform(pts1, pts2)
img_result = cv2.warpPerspective(img, matrix, (width, height))

# Highlight selected points
for x in range(0, 4):
    cv2.circle(img_reshaped, (int(pts1[x][0]), int(pts1[x][1])), 5, (0, 0, 255), cv2.FILLED)

# Output
cv2.imshow('Image', img_reshaped)
cv2.imshow('License plate', img_result)
cv2.waitKey(0)
