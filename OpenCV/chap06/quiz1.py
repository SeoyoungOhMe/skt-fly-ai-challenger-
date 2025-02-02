import numpy as np, cv2

image1 = cv2.imread("images/add1.jpg", cv2.IMREAD_GRAYSCALE)   # 영상 읽기
image2 = cv2.imread("images/add2.jpg", cv2.IMREAD_GRAYSCALE)
if image1 is None or image2 is None: raise Exception("영상 파일 읽기 오류 발생")

# 영상 합성
add_img3 = cv2.addWeighted(image1, 0.5, image2, 0.5, 0)

titles = ['image1','image2','add_img3']
for t in titles: cv2.imshow(t, eval(t))
cv2.waitKey(0)
