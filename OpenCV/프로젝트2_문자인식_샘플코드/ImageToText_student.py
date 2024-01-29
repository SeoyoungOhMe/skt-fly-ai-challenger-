import cv2
import numpy as np
import pytesseract

TESSERACT_PATH = "C:/Program Files/Tesseract-OCR/tesseract.exe" #테서렉스 설치 경로
imgpath='./images/2-1.jpg'  #이미지 파일 경로
win_name = "Image To Text"  #OpenCV 창 이름
img = cv2.imread(imgpath)   #이미지 읽어오기
img = cv2.resize(img, (720, 400)) #이미지 크기 조절
cnt = 0
pts = np.zeros((4, 2), dtype=np.int32)

#마우스 이벤트 처리 함수
def onMouse(event, x, y, flags, param):
    global pts, cnt, img
    if event == cv2.EVENT_LBUTTONDOWN:
        pts[cnt] = [x, y]
        cv2.circle(img, (x, y), 10, (0, 0, 255), -1)
        cv2.imshow(win_name, img)
        cnt += 1
        if cnt == 4:
            pts_new = reorderPts(pts)  #이미지 처리 함수 호출
            dw, dh = 720, 400
            pts = np.array([[0, 0], [0, dh], [dw, dh], [dw, 0]], np.float32)
            mtrx = cv2.getPerspectiveTransform(pts_new.astype(np.float32), pts.astype(np.float32))
            result = cv2.warpPerspective(img, mtrx, (img.shape[1], img.shape[0]))
            result = result[0:dh, 0:dw]

            result_th = cv2.threshold(cv2.cvtColor(result, cv2.COLOR_BGR2GRAY), 120, 255, cv2.THRESH_BINARY_INV)[1]

            text = GetOCR(result) 
            print(text)

            cv2.imshow('scanned', result_th)
            cv2.waitKey(0)


def reorderPts(pts):
    idx = np.lexsort((pts[:, 1], pts[:, 0]))  # 칼럼0 -> 칼럼1 순으로 정렬한 인덱스를 반환
    pts = pts[idx]  # x좌표로 정렬

    if pts[0, 1] > pts[1, 1]:
        pts[[0, 1]] = pts[[1, 0]]

    if pts[2, 1] < pts[3, 1]:
        pts[[2, 3]] = pts[[3, 2]]

    return pts

#OCR 함수
def GetOCR(img):
    #이미지 불러오기

    #OCR모델 불러오기
    pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

    #OCR모델로 글자 추출
    text = pytesseract.image_to_string(img, lang='kor+eng')
        
    return text

cv2.namedWindow(win_name)
cv2.imshow(win_name, img)   
cv2.setMouseCallback(win_name, onMouse)
cv2.waitKey(0)