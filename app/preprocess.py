import cv2
import numpy as np


# preprocess function
def filter(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    median = cv2.medianBlur(gray, 13) #13

    mean = cv2.blur(median, (11,11)) #7

    th3 = cv2.adaptiveThreshold(mean,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)

    th3 = cv2.bitwise_not(th3)

    kernel = np.ones((11, 11), np.uint8)  # 7
    final = cv2.dilate(th3, kernel, iterations=1)
    final = cv2.bitwise_not(final)

    cv2.imwrite("temp_storage/sinhalaprocessed.jpg", final)









