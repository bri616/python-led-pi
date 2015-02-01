#!/usr/bin/python

import RPi.GPIO as GPIO
import time

def change_led(letter):
  color = letter.lower()
  pin = ledpins[color]
  state = letter.isupper()
  GPIO.output(pin, state)

def all_leds_off():
  for pin in ledpins.values():
    GPIO.output(pin, False)


def parse_pattern(pattern):
  for light_event in pattern:
    for character in light_event:
      if character == "O":
       all_leds_off()
      elif character.isalpha():
        change_led(character)
      else:
        time.sleep(int(character))
        all_leds_off()
  
if __name__ == "__main__":
  # red led is in GPIO 17, blue is in 27, green is in 12
  ledpins = {"r": 11, "b": 13, "g": 12}

  # pattern string is Color and Persistence Time "R2" or "RGB3"
  # Red+Green, Red+Blue, Green+Blue, Red, Green, Blue, Red+Green+Blue, Off
  pattern = ["R2","G4","B2","BG1","O1","R2"]

  # setup GPIO using Board numbering

  GPIO.setmode(GPIO.BOARD)
  
  # set direction on leds and turn them all off
  for pin in ledpins.values():
    GPIO.setup(pin, GPIO.OUT)
  all_leds_off()

  parse_pattern(pattern)
