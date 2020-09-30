import cv2
import time
import argparse
parser = argparse.ArgumentParser(description='Test yolo data.')
parser.add_argument('-i', help='Image', dest='img', required=True)
parser.add_argument('-t', help='Yolo text file', dest='txt',required=True)

args = parser.parse_args()
#напишите путь к нужному вам изображению
frame = cv2.imread(args.img)
coordinates = []
with open(args.txt, "r") as lines:
	for line in lines:
		hT, wT, cT = frame.shape
		coordinates = line[2:].rstrip('\n').split(' ')
		x1, y1,w2,h2 = float(coordinates[0]), float(coordinates[1]), float(coordinates[2]), float(coordinates[3])
		print(x1,y1,w2,h2)
		w, h = int(w2 * wT), int(h2 * hT)
		x, y = int((x1 * wT) - w / 2), int((y1 * hT) - h / 2)
# # 0 1 2 3 x1 - центр по x в процентах y1- центр по y в процентах w1- центр по w в процентах h1- центр по h в процентах
		cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,255))
cv2.imshow("f", frame)
cv2.waitKey(0)  
