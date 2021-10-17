import cv2
import os

file = open("ac1_30fps.txt", 'r')
lines = file.readlines()
file.close()

frame_detector_count = -1
count = 0

for line in lines:

    count = count+1

    parts = line.split(",") # split line into parts

    frame=int(parts[0])

    img = cv2.imread("ac1_player_30fps/%d.jpg"%(frame))

    if(frame != frame_detector_count and not os.path.exists("/home/lunet/corq/Documents/Data/to_be_copied/AC1/cropped321/frame%d"%(frame))):
        frame_detector_count = frame
        os.mkdir("cropped321/frame%d"%frame)

    id=int(parts[1])
    x=int(parts[2])
    y=int(parts[3])
    w=int(parts[4])
    h=int(parts[5])

    if(y < 1000):
    	roi = img[y:y+h, x:x+w]
    	cv2.imwrite("/home/lunet/corq/Documents/Data/to_be_copied/AC1/cropped321/frame%d/%d.jpg"%(frame,count), roi)
    else:
	continue
