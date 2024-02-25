import time
from firebase import *
data = ["000000", "000100", "000001", "001100", "000111", "001100", "110000", "010000", "000000"]

#chunks = [data[x:x+4] for x in range(0, len(data), 100)]
#chunks = chunks[0]

batch = 1
for i in range(0, len(data), 4):
    letters = data[i:i+4]
    print(letters)
    msg = f'"Showing 4 braille letters at a time: Batch {batch} out of {-(len(data)//-4)}"'
    db.child("IOTGreenhouse").update({"braille_msg": msg})
    print(msg)
    batch = batch+1
    time.sleep(5)
db.child("IOTGreenhouse").update({"braille_msg": '"Translation Finished!"'})
