from codes import *
from motor import *
from texttobraille import *
from firebase import *
import time


# main loop starts here
try:
    print("Starting Program")
    while True:
        db.child("IOTGreenhouse").update({"braille_msg": '"Ready to Translate"'})
        text, display, reset = get_db()
        print(f'Text:{text}, Display:{display}, Reset:{reset}')
        if (reset != "true") and (display == "true"):
            display = "false"
            db.child("IOTGreenhouse").update({"braille_display": display})
            print("Displaying the letters:", text)
            display_text(text)
        elif (reset == "true"):
            reset = "false"
            db.child("IOTGreenhouse").update({"braille_reset": reset})
            print("Resetting Characters")
            reset_servo()
        else:
            print("Keeping Characters")
            time.sleep(0.5)
except KeyboardInterrupt:
    print("Stopped by the user")
finally:
    reset_servo()
    






