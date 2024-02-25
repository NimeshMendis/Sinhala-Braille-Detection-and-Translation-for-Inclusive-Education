import cv2
import numpy as np

from horizontal import *
from vertical import *
from classify import *
from classify_english import *
from brailletotext import *


def translate(preprocessed, language):

    detected = preprocessed.copy()
    rows = horizontal_segment(preprocessed)

    codes = []
    current_x = None
    eng_sentence = ""
    print("Translation Starting")

    # iterate through rows and individual cells in them in order to classify
    for x in rows:
        row = preprocessed[x[1]:x[1] + x[3], x[0]:x[0] + x[2], :]
        cells = column_segment(row)
        for y in cells:
            cell = preprocessed[x[1]:x[1] + y[3], y[0]:y[0] + y[2], :]

            # rectangle around detected cells
            cv2.rectangle(detected, (y[0], x[1]), (y[0] + y[2], x[1] + y[3]), (0, 0, 255), 2)

            # Call CNN if that method is selected
            if language == "English(CNN)":
                eng_sentence += predict(cell)
            # else use image processing classify function
            else:
                codes.append(classify(cell))

                # add spaces between braille cells
                if current_x:
                    print(y[0] - current_x)
                    if (y[0] - current_x) > 190 or (y[0] - current_x) < -160:
                        codes.insert(len(codes)-1, "000000")
                    if (y[0] - current_x) < -160:
                        codes.insert(len(codes) - 1, "222222")
                    current_x = y[0]
                else:
                    current_x = y[0]


    print(codes)
    if language == "English(CNN)":
        translated = eng_sentence
    elif language == "English":
        translated = translate_to_text_eng(codes)
    else:
        translated = translate_to_text(codes)
    print(translated)
    print(language)

    return detected, translated








