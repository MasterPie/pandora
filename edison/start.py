#!/usr/bin/env python

import mraa
import time
import os
import thread
import random

is_active = False

#PINS
progress_pin = mraa.Gpio(8)
progress_pin.dir(mraa.DIR_OUT)

flash_pin = mraa.Gpio(9)
flash_pin.dir(mraa.DIR_OUT)

closebtn_pin = mraa.Gpio(2)
closebtn_pin.dir(mraa.DIR_IN)

clearbtn_pin = mraa.Gpio(4)
clearbtn_pin.dir(mraa.DIR_IN)

##CANDLE_LED
can_green_pin = mraa.Gpio(13)
can_green_pin.dir(mraa.DIR_OUT)

can_blue_pin = mraa.Gpio(12)
can_blue_pin.dir(mraa.DIR_OUT)

can_red_pin = mraa.Gpio(11)
can_red_pin.dir(mraa.DIR_OUT)

def blink_progress():
	is_active = True
	while is_active:
		progress_pin.write(1)
		time.sleep(0.05)
		progress_pin.write(0)
		time.sleep(0.05)
	progress_pin.write(1)

is_candle_active = False

def do_calm_candle(revenge):
	can_red_pin.write(0)
	can_blue_pin.write(0)
	if revenge > 0.5:
		can_red_pin.write(1)
	else:
		can_blue_pin.write(1)
	
def do_faces():
	flash_pin.write(1)
	os.system("python extract_faces.py haarcascade_frontalface_default.xml")
	flash_pin.write(0)

def do_clear():
	os.system("python clear.py")

already_pressed = False

while True:
	progress_pin.write(1)
	do_calm_candle(0.4)
	if closebtn_pin.read() and already_pressed == False:
		already_pressed = True
		is_candle_active = False
		thread.start_new_thread(blink_progress, ())
		do_faces()
		is_active = False
		thread.start_new_thread(do_calm_candle, (255,))
	if closebtn_pin.read() == 0:
		already_pressed = False

	if clearbtn_pin.read():
		thread.start_new_thread(blink_progress,())
		do_clear()
		is_active = False
	progress_pin.write(1)
