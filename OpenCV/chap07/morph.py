import numpy as np, cv2
image = cv2.imread("images/morph.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")
mask = np.array([[0, 1, 0], # 마스크 초기화
[1, 1, 1],
[0, 1, 0]]).astype("uint8")
th_img = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)[1]
dst1 = cv2.morphologyEx(th_img, cv2.MORPH_OPEN, mask) # OpenCV의 열림 함수
dst2 = cv2.morphologyEx(th_img, cv2.MORPH_CLOSE, mask, iterations = 1) 
cv2.imshow("OpenCV opening", dst1); cv2.imshow("OpenCV closing", dst2)
cv2.waitKey(0)