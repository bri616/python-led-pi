#!/usr/bin/python

import RPi.GPIO as GPIO
import time

#setup GPIO using Board numbering

GPIO.setmode(GPIO.BOARD)

# have the led plugged into the pi's GPIO17
pin = 11

GPIO.setup(pin, GPIO.OUT)

while True:
  GPIO.output(pin, True)
  time.sleep(1)
  GPIO.output(pin, False)
  time.sleep(0.5)
 

