import cv2
import time
import argparse
parser = argparse.ArgumentParser(description='Test yolo data.')
parser.add_argument('-i', help='Image', dest='img', required=True)
parser.add_argument('-t', help='Yolo text file', dest='txt',required=True)

args = parser.parse_args()
frame = cv2.imread(args.img)
cv2.namedWindow("f", cv2.WINDOW_NORMAL);

coordinates = []
with open(args.txt, "r") as lines:
	for line in lines:
		hT, wT, cT = frame.shape
		coordinates = line.rstrip('\n').split(' ')
		idx = coordinates[0]	
		x1, y1,w2,h2 = float(coordinates[1]), float(coordinates[2]), float(coordinates[3]), float(coordinates[4])
		print(x1,y1,w2,h2)
		w, h = int(w2 * wT), int(h2 * hT)
		x, y = int((x1 * wT) - w / 2), int((y1 * hT) - h / 2)
# # 0 1 2 3 x1 - центр по x в процентах y1- центр по y в процентах w2- центр по w в процентах h2- центр по h в процентах
		cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,255), 2)
		cv2.putText(frame,str(idx), (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (128, 0, 255), 2)
cv2.imshow("f", frame)
cv2.waitKey(0)  


# import cv2
# import time
# import argparse
# import numpy as np
# import matplotlib.pyplot as plt
# parser = argparse.ArgumentParser(description='Test yolo data.')
# parser.add_argument('-i', help='Image', dest='img', required=True)
# parser.add_argument('-t', help='Yolo text file', dest='txt',required=True)
# parser.add_argument('-l', help='labels txt file', dest='label',required=True)
# args = parser.parse_args()
# frame = cv2.imread(args.img)
# cv2.namedWindow("f", cv2.WINDOW_NORMAL);

# coordinates = []

# with open(args.txt, "r") as lines:
# 	for line in lines:
# 		hT, wT, cT = frame.shape
# 		coordinates = line.rstrip('\n').split(' ')
# 		idx = coordinates[0]	
# 		x1, y1,w2,h2 = float(coordinates[1]), float(coordinates[2]), float(coordinates[3]), float(coordinates[4])
# 		print(x1,y1,w2,h2)
# 		cmap = plt.get_cmap('tab20b')
# 		colors = [cmap(i)[:3] for i in np.linspace(0, 1, 20)]
# 		color = colors[int(idx) % len(colors)]
# 		color = [i * 255 for i in color]
# 		w, h = int(w2 * wT), int(h2 * hT)
# 		x, y = int((x1 * wT) - w / 2), int((y1 * hT) - h / 2)
# 		with open(args.label, "r") as labels:
# 			classNames = labels.read().rstrip('\n').split('\n') 
# # # 0 1 2 3 x1 - центр по x в процентах y1- центр по y в процентах w2- центр по w в процентах h2- центр по h в процентах
# 			cv2.rectangle(frame, (x,y), (x+w, y+h), color,3)
# 			print(len(classNames[1]))
# 			cv2.rectangle(frame, (x,y-30), (x+len(classNames[int(idx)]*15), y), color,-1)
# 			cv2.putText(frame,str(classNames[int(idx)]), (x+4, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
# cv2.imshow("f", frame)
# cv2.waitKey(0)  
