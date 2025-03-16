import pyrebase

firebaseConfig = {
    "apiKey": "",
    "authDomain": "",
    "databaseURL": "",
    "storageBucket": ""
}

firebase = pyrebase.initialize_app(firebaseConfig)