import cv2
import numpy as np
import math


# function for segmenting rows
def horizontal_segment(img):
    img2 = img.copy()

    th2 = cv2.bitwise_not(img)
    r, c, w = th2.shape

    horizontalstructure = cv2.getStructuringElement(cv2.MORPH_RECT, (c + 2000, 40))
    horizontal = cv2.dilate(th2, horizontalstructure, (-1, -1))

    horizontal = cv2.cvtColor(horizontal,cv2.COLOR_BGR2GRAY)
    ret, thresh1 = cv2.threshold(horizontal, 127, 255, cv2.THRESH_BINARY)

    contours, hierarchy = cv2.findContours(thresh1 ,
                                           cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

    print("Number of Contours found = " + str(len(contours)))


    hmax = 0
    for c in contours:
        cnt = c
        x,y,w,h = cv2.boundingRect(cnt)
        print(x,y,w,h)
        if h > hmax :
            hmax = h

    rows = []

    for c in contours:
        cnt = c
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(img2,(x,y),(x+w,y+hmax),(0,0,255),2)
        numpy_row = np.array([x,y,w,hmax])
        rows.append(numpy_row)

    rows.reverse()
    return rows









