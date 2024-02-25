import pyrebase
from texttobraille import *

firebaseConfig = {
    "apiKey": "AIzaSyA1cZhgLy_rE6I23zvKhg4Gy3LpfJJJ6tk",
    "authDomain": "greenhouseautomation-8af0f.firebaseapp.com",
    "databaseURL": "https://greenhouseautomation-8af0f-default-rtdb.firebaseio.com",
    "storageBucket": "greenhouseautomation-8af0f.appspot.com"
}

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

# braille = "පාසල"
#braille_display = "true"
# braille_reset = "false"
#
# db.child("IOTGreenhouse").update({"braille": braille})
# db.child("IOTGreenhouse").update({"braille_display": braille_display})
# db.child("IOTGreenhouse").update({"braille_reset": braille_reset})
#
#
# print("Finished")
#
# def filter_str(string_unfiltered):
#     string_filtered = string_unfiltered.replace('"', '')
#     return string_filtered
# a = filter_str(db.child("IOTGreenhouse").child("braille").get().val())
# b = filter_str(db.child("IOTGreenhouse").child("braille_display").get().val())
# c = filter_str(db.child("IOTGreenhouse").child("braille_reset").get().val())

# print(translate_to_braille(normalize(a)))


