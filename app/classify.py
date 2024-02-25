import cv2
import numpy as np


def classify(img):
    h, w, channels = img.shape
    reg1 = img[0:int(h / 3), 0:int(w / 2 )]
    reg2 = img[int(h / 3): int(2 * h/ 3), 0:int(w / 2)]
    reg3 = img[int(2 * h / 3): int(h), 0:int(w / 2)]
    reg4 = img[0:int(h / 3), int(w / 2):int(w)]
    reg5 = img[int(h / 3): int(2 * h / 3), int(w / 2):int(w)]
    reg6 = img[int(2 * h / 3): int(h), int(w / 2):int(w)]

    regions = [reg1, reg2, reg3, reg4, reg5, reg6]
    # print(np.sum(reg1 == 0) / np.sum(reg1 == 255))

    classified_character_code = ""
    for x in regions:
        black_pixel_ratio = np.sum(x == 0) / np.sum(x == 255)
        if (black_pixel_ratio > 0.05):
            region_code = "1"
        else:
            region_code = "0"
        classified_character_code += region_code

    return classified_character_code



