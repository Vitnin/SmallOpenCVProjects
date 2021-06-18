import cv2


# Method to treat the image in general
def getContours(img_):
    contours, hierarchy = cv2.findContours(img_, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)

        # Eliminating noises
        if area > 100:
            cv2.drawContours(img_contour, cnt, -1, (255, 0, 255), 2)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            obj_cor = len(approx)
            print(obj_cor)
            x, y, w, h = cv2.boundingRect(approx)

            # Classify geometric shape
            if obj_cor == 3:
                object_type = 'Tri'
            elif obj_cor == 4:
                asp_ratio = w/float(h)
                if 0.95 < asp_ratio < 1.05:
                    object_type = 'Squ'
                else:
                    object_type = 'Rec'
            elif obj_cor == 6:
                object_type = 'Hex'
            else:
                object_type = 'Sph'

            # Drawing on the image
            cv2.rectangle(img_contour, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(img_contour, object_type,
                        (x + (w//2) - 10, y + (h//2)-50), cv2.FONT_HERSHEY_COMPLEX, 0.4,
                        (50, 255, 50), 1)


# Initial treatment of the image
path = 'images/shapes.jpg'
img = cv2.imread(path)
img = cv2.resize(img, (512, 327))

img_contour = img.copy()
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (7, 7), 1)
img_canny = cv2.Canny(img_blur, 50, 50)

getContours(img_canny)

# Showing off
cv2.imshow('Original', img)
cv2.imshow('Canny', img_canny)
cv2.imshow('Contour', img_contour)
print(img.shape)
cv2.waitKey(0)
