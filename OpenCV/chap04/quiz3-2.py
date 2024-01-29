import numpy as np
import cv2

img = cv2.imread('images\circle_img.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
height, width, channels = img.shape

net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
classes = ['red', 'green', 'blue']

layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]