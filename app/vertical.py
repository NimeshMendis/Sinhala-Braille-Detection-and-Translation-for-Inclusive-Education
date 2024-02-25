import cv2
import numpy as np


# function for segmenting braille cells
def column_segment(img):

    img2 = img.copy()
    th2 = cv2.bitwise_not(img)
    r, c, w = th2.shape

    structuringelement = cv2.getStructuringElement(cv2.MORPH_RECT, (36, r + r))
    vertical = cv2.dilate(th2, structuringelement, (-1, -1))

    vertical = cv2.cvtColor(vertical, cv2.COLOR_BGR2GRAY)

    ret, thresh1 = cv2.threshold(vertical, 127, 255, cv2.THRESH_BINARY)

    contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    print("Number of Contours found = " + str(len(contours)))

    # determine maximum width of braille cell
    wmax = 0
    for c in contours:
        cnt = c
        x, y, w, h = cv2.boundingRect(cnt)
        if w > wmax:
            wmax = w

    cells = []

    for c in contours:
        cnt = c
        x, y, w, h = cv2.boundingRect(cnt)
        numpy_cell = np.array([x, y, wmax, h])
        cv2.rectangle(img2, (x, y), (x + wmax, y + h), (0, 0, 255), 1)
        cells.append(numpy_cell)

    cells.reverse()

    return cells
