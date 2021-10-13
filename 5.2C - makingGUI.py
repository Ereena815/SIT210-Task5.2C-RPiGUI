##
#    Embedded Systems Development
#    Exercise : Task 5.2C - Making GUI
#    Name : Ereena Bagga
#    Student ID : 2010993040
##

from tkinter import *
import tkinter.font as FONT
import RPi.GPIO as GPIO
from gpiozero import LED

# Use "GPIO" pin numbering
GPIO.setmode(GPIO.BCM)

# Pin Definitions
redLED = LED(12)
yellowLED = LED(7)
greenLED = LED(8)

# GUI Defintions
win = Tk()
win.title("LED CONTROLLER")
myFont = FONT.Font(family = 'Helvetica', size = 14, weight = 'bold')

# Event Functions

# This method toggles the red LED. If red led is on, turn it off. Else, turn red led on and the other leds off
def redLedToggle():
    if redLED.is_lit:
        redLED.off()
        redLedButton["text"] = "TURN RED LED ON"
    else:
        redLED.on()
        redLedButton["text"] = "TURN RED LED OFF"
        yellowLED.off()
        yellowLedButton["text"] = "TURN YELLOW LED ON"
        greenLED.off()
        greenLedButton["text"] = "TURN GREEN LED ON"

# This method toggles the yellow LED. If yellow led is on, turn it off. Else, turn yellow led on and the other leds off
def yellowLedToggle():
    if yellowLED.is_lit:
        yellowLED.off()
        yellowLedButton["text"] = "TURN YELLOW LED ON"
    else:
        yellowLED.on()
        yellowLedButton["text"] = "TURN YELLOW LED OFF"
        redLED.off()
        redLedButton["text"] = "TURN RED LED ON"
        greenLED.off()
        greenLedButton["text"] = "TURN GREEN LED ON"

# This method toggles the green LED. If green led is on, turn it off. Else, turn green led on and the other leds off
def greenLedToggle():
    if greenLED.is_lit:
        greenLED.off()
        greenLedButton["text"] = "TURN GREEN LED ON"
    else:
        greenLED.on()
        greenLedButton["text"] = "TURN GREEN LED OFF"
        redLED.off()
        redLedButton["text"] = "TURN RED LED ON"
        yellowLED.off()
        yellowLedButton["text"] = "TURN YELLOW LED ON"       

# This method destroys the window and sets the GPIO pins back to their intial settings
def close():
    GPIO.cleanup()
    win.destroy()
    
# Widgets
redLedButton = Button(win, text = 'TURN RED LED ON', font = myFont, command = redLedToggle, bg = 'red', height = 2, width = 30)
redLedButton.grid(row = 0, column = 1)

yellowLedButton = Button(win, text = 'TURN YELLOW LED ON', font = myFont, command = yellowLedToggle, bg = 'yellow', height = 2, width = 30)
yellowLedButton.grid(row = 1, column = 1)

greenLedButton = Button(win, text = 'TURN GREEN LED ON', font = myFont, command = greenLedToggle, bg = 'green', height = 2, width = 30)
greenLedButton.grid(row = 2, column = 1)

exitButton = Button(win, text = 'EXIT', font = myFont, command = close, bg = 'bisque2', height = 2, width = 15)
exitButton.grid(row = 1, column = 2)

win.protocol("WM_DELETE_WINDOW",close) # exit cleanly
win.mainloop() # loop forever