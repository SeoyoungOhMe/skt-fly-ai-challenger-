import numpy as np, cv2

def onChange(value):
    global image,title
    add_value = value - int(image[0][0])
    image = image + add_value
    cv2.imshow(title, image)

image = cv2.imread("images/canny.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일 읽기 오류")


canny2 = cv2.Canny(image, 100, 150) # OpenCV 캐니 에지


cv2.imshow("image", image)
title = "OpenCV_Canny"
cv2.imshow(title, canny2) # OpenCV 캐니 에지
cv2.createTrackbar('th1', title, image[0][0], 50, onChange)
cv2.waitKey(0)