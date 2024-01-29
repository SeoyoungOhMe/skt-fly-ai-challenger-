import numpy as np
import cv2
#import pandas as pd
#import matplotlib.pyplot as plt

red, blue, green = (0,0,255),(255,0,0),(0,255,0)
image = np.full((480, 640, 3), (255, 255, 255), np.uint8)             # 

center = ( image.shape[1]//2, image.shape[0]//2 )         		# 
pt1, pt2 = (300, 50), (100, 220)
pt3, pt4 = (200, 300), (400, 270)
pt5 = (500, 100)                      # 그림자 좌표

cv2.circle( image, pt1, 40, red, -1  )                         #  
cv2.circle(  image, pt2, 50, blue, -1 )
cv2.circle( image, pt3, 70, green, -1 )     
cv2.circle( image, pt4, 60, blue, -1  )
cv2.circle( image, pt5, 50, red, -1  ) 


image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
height, width, channels = image.shape

net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
layer_names = net.getLayerNames()




title = "Draw circles"
cv2.namedWindow(title)
cv2.imshow(title, image)
cv2.waitKey(0)
