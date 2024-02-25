import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyA1cZhgLy_rE6I23zvKhg4Gy3LpfJJJ6tk",
    "authDomain": "greenhouseautomation-8af0f.firebaseapp.com",
    "databaseURL": "https://greenhouseautomation-8af0f-default-rtdb.firebaseio.com",
    "storageBucket": "greenhouseautomation-8af0f.appspot.com"
}

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

def filter_str(text):
    filtered_str = text.replace('"','')
    return filtered_str

#braille = "පාසල"
#braille_reset = "false"


#db.child("IOTGreenhouse").update({"braille_reset": braille_reset})

def get_db():
    text = filter_str(db.child("IOTGreenhouse").child("braille").get().val())
    display = filter_str(db.child("IOTGreenhouse").child("braille_display").get().val())
    reset = filter_str(db.child("IOTGreenhouse").child("braille_reset").get().val())
    return text, display, reset




