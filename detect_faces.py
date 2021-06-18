import cv2

# Importing assets
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
img = cv2.imread('images/men.jpg')
img = cv2.resize(img, (512, 314))

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(img_gray, 1.1, 2)

# Tagging all faces in the photo
for(x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (250, 0, 0), 2)

# Showing
cv2.imshow('Gray image', img_gray)
cv2.imshow('Men', img)
cv2.waitKey(0)
