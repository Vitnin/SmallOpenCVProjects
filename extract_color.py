import cv2
import numpy as np


def empty(a):
    pass


# Image to be analyzed
path = 'images/car.jpg'

# Creation of trackbars
cv2.namedWindow('TrackBars')
cv2.resizeWindow('TrackBars', 640, 240)
cv2.createTrackbar('HueMin', 'TrackBars', 0, 179, empty)
cv2.createTrackbar('HueMax', 'TrackBars', 86, 179, empty)
cv2.createTrackbar('SatMin', 'TrackBars', 0, 255, empty)
cv2.createTrackbar('SatMax', 'TrackBars', 255, 255, empty)
cv2.createTrackbar('ValMin', 'TrackBars', 0, 255, empty)
cv2.createTrackbar('ValMax', 'TrackBars', 255, 255, empty)

# Image treatment
img = cv2.imread(path)
img = cv2.resize(img, (320, 320))
img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Exhibition
while True:
    h_min = cv2.getTrackbarPos('HueMin', 'TrackBars')
    h_max = cv2.getTrackbarPos('HueMax', 'TrackBars')
    s_min = cv2.getTrackbarPos('SatMin', 'TrackBars')
    s_max = cv2.getTrackbarPos('SatMax', 'TrackBars')
    v_min = cv2.getTrackbarPos('ValMin', 'TrackBars')
    v_max = cv2.getTrackbarPos('ValMax', 'TrackBars')
    print(h_min, h_max, s_min, s_max, v_min, v_max)
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(img_HSV, lower, upper)
    img_result = cv2.bitwise_and(img, img, mask=mask)

    img_hor = np.hstack((img, img_HSV, img_result))

    cv2.imshow('Overview', img_hor)
    cv2.imshow('Mask', mask)
    if cv2.waitKey(32) & 0XFF == ord('q'):
        break
