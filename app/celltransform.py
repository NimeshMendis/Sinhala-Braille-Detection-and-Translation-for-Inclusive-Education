import cv2
import numpy as np


def convert_to_cell_size(image: np.ndarray):
    image_extended = np.full((image.shape[0],image.shape[1]*2, image.shape[2]), 255, dtype=np.uint8)
    image_extended[0:0 + image.shape[0], 0:0 + image.shape[1]] = image
    return image_extended

