#!/usr/bin/python

import RPi.GPIO as GPIO

#setup GPIO using Board numbering

GPIO.setmode(GPIO.BOARD)

# have the led plugged into the pi's GPIO17
ledpin = 11
buttonpin = 3

GPIO.setup(ledpin, GPIO.OUT)
GPIO.setup(buttonpin, GPIO.IN)

def is_pressed(pin):
  return not GPIO.input(pin)

while True:
  print GPIO.input(buttonpin)
  # if button is depressed(0):
  # if not GPIO.input(buttonpin):
  if is_pressed(buttonpin):
    # turn on led
    GPIO.output(ledpin, True)
  else:
    # turn off led
    GPIO.output(ledpin, False)


 

