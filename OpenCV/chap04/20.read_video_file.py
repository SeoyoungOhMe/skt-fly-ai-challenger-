import cv2
from Common.utils import put_string
import numpy as np

capture = cv2.VideoCapture("images/move_file.avi")		# 동영상 파일 개방
if not capture.isOpened(): raise Exception("동영상 파일 개방 안됨")		# 예외 처리

frame_rate = capture.get(cv2.CAP_PROP_FPS)           		# 초당 프레임 수
delay = int(1000 / frame_rate)                         		# 지연 시간
frame_cnt = 0                                       		# 현재 프레임 번호


while True:
	ret, frame = capture.read()
	if not ret or cv2.waitKey(delay) >= 0: break
	cv2.rectangle(frame, (200, 100, 200, 100), (0, 0, 255), 3)
 
	blue, green, red = cv2.split(frame)
	cv2.add(green[100:300, 200:300], 50, green[100:300, 200:300])
 
	# if 100 <= frame_cnt < 200: 
    # 	cv2.add(blue, 100, blue)
	# elif 200 <= frame_cnt < 300 : 
    #  	cv2.add(green, 100, green,50)
      
	# elif 200 <= frame_cnt < 400 : 
    #  	cv2.add(red, 100, red)
	
	frame = cv2.merge( [blue, green, red] )                 # 단일채널 영상 합성
	# put_string(frame, "frame_cnt : ", (20, 320), frame_cnt)
	cv2.imshow("Read Video File", frame)

capture.release()