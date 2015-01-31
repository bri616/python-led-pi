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

def turn_on(pin):
  GPIO.output(pin, True)

def turn_off(pin):
  GPIO.output(pin, False)  
  

while True:
  if is_pressed(buttonpin):
    turn_on(ledpin)
  else:
    turn_off(ledpin)

 

