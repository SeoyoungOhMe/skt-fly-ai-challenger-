import numpy as np, cv2


def salt_pepper_noise(img, n):
    h, w = img.shape[:2]
    x, y = np.random.randint(0, w, n), np.random.randint(0, h, n)
    noise = img.copy()
    for (x,y) in zip(x,y):
        noise[y, x] = 0 if np.random.rand() < 0.5 else 255
        return noise

image = cv2.imread("images/median2.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")
    
noise = salt_pepper_noise(image, 500)
med_img2 = cv2.medianBlur(noise, 3) 


data = [0, 1, 0,
1, 1, 1,
0, 1, 0]
mask = np.array(data, np.uint8).reshape(3, 3)
th_img = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)[1]
dst2 = cv2.erode(th_img, mask)


mask2 = np.array([[0, 1, 0],
[1, 1, 1],
[0, 1, 0]]).astype("uint8")
th_img = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)[1]
dst3 = cv2.morphologyEx(th_img, cv2.MORPH_DILATE, mask2) 


cv2.imwrite('chap07/images/noise.jpg', noise)

cv2.imshow("image", image),
cv2.imshow("noise", noise),
cv2.imshow("median - OpenCV", med_img2)

cv2.imshow("OpenCV erode", dst2)

cv2.imshow("OpenCV dilate", dst3)
cv2.waitKey(0)