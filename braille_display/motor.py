from adafruit_servokit import ServoKit
from codes import *
import RPi.GPIO as GPIO
from texttobraille import *
from firebase import *
import time


        
kit = ServoKit(channels=16)


kit.servo[0].set_pulse_width_range(500,2500)
kit.servo[1].set_pulse_width_range(800,2200)
kit.servo[2].set_pulse_width_range(800,2200)
kit.servo[3].set_pulse_width_range(500,2500)
kit.servo[4].set_pulse_width_range(500,2500)
kit.servo[5].set_pulse_width_range(800,2200)
kit.servo[6].set_pulse_width_range(800,2200)
kit.servo[7].set_pulse_width_range(500,2500)

def reset_servo_90():
    for i in range(8):
        kit.servo[i].angle = 90
        time.sleep(1)
        GPIO.cleanup()
        
def reset_servo():
    res_signals = [a0[1], a1[1], a2[1], a3[1], a4[1], a5[1], a6[1], a7[1]]
    for i in range(8):
        kit.servo[i].angle = res_signals[i]
        time.sleep(0.5)
        GPIO.cleanup()
    
    
def split_str(text):
    a = text[0:len(text)//2]
    b = text[len(text)//2:]
    return a,b

def move_sliders(signals):
    for x in range(8):
        kit.servo[x].angle = signals[x]
        time.sleep(0.5)

     
def display_text(text):
    _, input_text = translate_to_braille(normalize(text))


    batch = 1
    for i in range(0, len(input_text), 4):
        letters = input_text[i:i+4]
        
        msg = f'"Showing 4 braille letters at a time: Batch {batch} out of {-(len(input_text)//-4)}"'
        db.child("IOTGreenhouse").update({"braille_msg": msg})
        print(msg)
        batch = batch+1
        
        if (1 > len(letters)):
            s0,s1 = "000","000"
        else:
            s0, s1 = split_str(letters[0])
        if (2 > len(letters)):
            s2,s3 = "000","000"
        else:
            s2, s3 = split_str(letters[1])
        if (3 > len(letters)):
            s4,s5 = "000","000"
        else:
            s4, s5 = split_str(letters[2])
        if (4 > len(letters)):
            s6,s7 = "000","000"
        else:
            s6,s7 = split_str(letters[3])


        #print(a4[codes.index(input)])

        s0 =  a0[codes.index(s0)]
        s1 =  a1[codes.index(s1)]
        s2 =  a2[codes.index(s2)]
        s3 =  a3[codes.index(s3)]
        s4 =  a4[codes.index(s4)]
        s5 =  a5[codes.index(s5)]
        s6 =  a6[codes.index(s6)]
        s7 =  a7[codes.index(s7)]


        signals = [s0,s1,s2,s3,s4,s5,s6,s7]


        #print(text)
        #print(letters)
        #print(signals)

        move_sliders(signals)
        time.sleep(5)
    db.child("IOTGreenhouse").update({"braille_msg": '"Translation Finished"'})




#reset_servo()
    
    






