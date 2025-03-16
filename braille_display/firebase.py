import pyrebase

firebaseConfig = {
    "apiKey": "",
    "authDomain": "",
    "databaseURL": "",
    "storageBucket": ""
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