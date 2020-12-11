#!/usr/bin/env python

import numpy as np
import cv2 as cv2
import random
import sys


img = np.full((512,512,3), 255, np.uint8)


#im = cv.CreateImage((100,100), cv.IPL_DEPTH_8U, 1);


# Compute surfaces

trees = [(50,"ch"),(50,"he"),(25,"ct"),(25,"me"),(50,"cr")]
colors = {
  "ch": (0,0,0),
  "he": (255,0,0),
  "ct": (0,255,0),
  "me": (0,0,255),
  "cr": (255,255,0),
}

# Built list
l = []
for (number,kind) in trees:
    for index in range(0,number):
        l.append(kind)

random.shuffle(l)

points = []
for t in l:
    x = int(random.uniform(0.,1.)*512)
    y = int(random.uniform(0.,1.)*512)
    points.append((x,y,t))

#print(len(points))
#sys.exit(0)


# Draw
for x,y,kind in points:
    cv2.line(img,(x-5,y),(x+5,y),colors[kind],1)
    cv2.line(img,(x,y-5),(x,y+5),colors[kind],1)

cv2.namedWindow("Input")
cv2.imshow("Input", img)
cv2.waitKey()

print(points)



