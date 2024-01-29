import numpy as np, cv2

def onThreshold(value):
    th[0] = cv2.getTrackbarPos("Hue_th1", "result")
    th[1] = cv2.getTrackbarPos("Hue_th2", "result")
    _, result = cv2.threshold(hue, th[1], 255, cv2.THRESH_TOZERO_INV)
    cv2.threshold(result, th[0], 255, cv2.THRESH_BINARY, result)

    cv2.imshow("result", result)


image1 = cv2.imread("images/add1.jpg", cv2.IMREAD_GRAYSCALE)   # 영상 읽기
image2 = cv2.imread("images/add2.jpg", cv2.IMREAD_GRAYSCALE)
if image1 is None or image2 is None: raise Exception("영상 파일 읽기 오류 발생")

# 영상 합성
add_img3 = cv2.addWeighted(image1, 0.5, image2, 0.5, 0)

titles = ['image1','image2','add_img3']
for t in titles: cv2.imshow(t, eval(t))

HSV_img = cv2.cvtColor(add_img3, cv2.COLOR_BGR2HSV)
hue = np.copy(HSV_img[:, :, 0])

th = [50, 100]
cv2.createTrackbar("Hue_th1","result", th[0], 255, onThreshold )
cv2.createTrackbar("Hue_th2","result", th[1], 255, onThreshold )
onThreshold(th[0])
cv2.imshow("BGR_img", add_img3)
cv2.waitKey(0)
