#### IMPORTING LIBRARIES ####

from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

#### ASSIGNING THE LED's ####

led = LED(18)
led1 = LED(23)
led2 = LED(24)

#### CREATING WINDOWS/GUI DEFINATION ####

win = Tk()
win.title("LED toggler")
my_font = tkinter.font.Font(family = 'Helvetica', size = 12, weight ="bold")

#### FUNCTIONS ####

def ledToggle():
	if led.is_lit:
		led.off()
		ledButton["text"] = "Turn LED on"
	else:
		led.on()
		ledButton["text"] = "Turn LED off"

def ledToggle1():
	if led1.is_lit:
		led1.off()
		ledButton1["text"] = "Turn LED on"
	else:
		led1.on()
		ledButton1["text"] = "Turn LED off"

def ledToggle2():
	if led2.is_lit:
		led2.off()
		ledButton2["text"] = "Turn LED on"
	else:
		led2.on()
		ledButton2["text"] = "Turn LED off"

def close():
	RPi.GPIO.cleanup()
	win.destroy()

#### TABS/WIDGETS ####

ledButton = Button(win, text = 'Turn LED on', font = my_font, command = ledToggle, bg = 'bisque2', height = 1, width = 24)
ledButton.grid(row = 0 , column = 1)

ledButton1 = Button(win, text = 'Turn LED on', font = my_font, command = ledToggle1, bg = 'bisque2', height = 1, width = 24)
ledButton1.grid(row = 1 , column = 1)

ledButton2 = Button(win, text = 'Turn LED on', font = my_font, command = ledToggle2, bg = 'bisque2', height = 1, width = 24)
ledButton2.grid(row = 2 , column = 1)

exitButton = Button(win, text = 'Exit', font = my_font, command = close, bg = 'red', height = 1, width = 6)
exitButton.grid(row = 3, column = 1)

#### CLOSING THE WINDOW CLEANLY ####

win.protocol("WM_DELETE_WINDOW", close)

#### INFINITE/NEVER-ENDING LOOP ####

win.mainloop()
