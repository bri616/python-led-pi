#!/usr/bin/python

import RPi.GPIO as GPIO
import time

if __name__ == "__main__":
  # red led is in GPIO 17, blue is in 27, green is in 18
  ledpins = {"r": 11, "b": 13, "g": 12}

  # setup GPIO using Board numbering

  GPIO.setmode(GPIO.BOARD)
  
  # set direction on leds and turn them all off
  for pin in ledpins.values():
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, False)
