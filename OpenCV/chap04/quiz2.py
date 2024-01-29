import numpy as np
import cv2

def onMouse(event, x, y, flags, param):                         # 콜백 함수 – 이벤트 내용 출력
    global title, image
    
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.rectangle(image, (x,y,x+30,y+30), (0,0,0), 3)
        cv2.imshow(title1, image)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(image, (x,y), 30, (0, 0, 0))
        cv2.imshow(title1, image)

image = np.full((200, 300), 255, np.uint8)                      # 

title1= "Mouse Event1"     #
cv2.imshow(title1, image) # 영상 보기

cv2.setMouseCallback('Mouse Event1', onMouse)     	# 마우스 콜백 함수

cv2.waitKey(0)                                      # 
cv2.destroyAllWindows()                             # 