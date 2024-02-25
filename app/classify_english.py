import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import load_model

import PIL
import cv2

from texttobraille import *


savedModel=load_model('model/Braille_model_eng.h5')


# filter unnecessary chars out of the predictions from CNN
def filter_pred(string_unfiltered):
    string_filtered = string_unfiltered.replace('[', '')
    string_filtered = string_filtered.replace(']', '')
    string_filtered = string_filtered.replace("'", '')
    return string_filtered


# get predictions from CNN
def predict(img):
    img2 = cv2.resize(img, (28, 28),
                   interpolation = cv2.INTER_AREA)
    img2 = img2/255.0
    x=np.expand_dims(img2,axis=0)
    pred_index =np.argmax(savedModel.predict(x), axis=1)
    pred = filter_pred(str(eng_alphabet[pred_index+1]))
    char = filter_pred(str(braille_eng[pred_index+1]))
    print(pred)
    return pred

