#!/usr/bin/python

import RPi.GPIO as GPIO
import time, math

if __name__ == "__main__":
  # red led is in GPIO 17, blue is in 27, green is in 18
  ledpins = {"r": 11, "b": 13, "g": 12}
  red = ledpins["r"]
  blue = ledpins["b"]
  green = ledpins["g"]

  # setup GPIO using Board numbering

  GPIO.setmode(GPIO.BOARD)
  
  # set direction on leds and turn them all off
  for pin in ledpins.values():
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, False)

  Freq = 100 #Hz  
   
  #setup all the colours  
  RED = GPIO.PWM(red, Freq) #Pin, frequency  
  RED.start(0) #Initial duty cycle of 0, so off  
  GREEN = GPIO.PWM(green, Freq)    
  GREEN.start(0)   
  BLUE = GPIO.PWM(blue, Freq)  
  BLUE.start(0)  
   
  def colour(R, G, B, on_time):  
    #colour brightness range is 0-100  
    RED.ChangeDutyCycle(R)  
    GREEN.ChangeDutyCycle(G)  
    BLUE.ChangeDutyCycle(B)  
    time.sleep(on_time)  
   
    #turn everything off  
    RED.ChangeDutyCycle(0)  
    GREEN.ChangeDutyCycle(0)  
    BLUE.ChangeDutyCycle(0)  
   
  def PosSinWave(amplitude, angle, frequency):  
    #angle in degrees  
    #creates a positive sin wave between 0 and amplitude*2  
    return amplitude + (amplitude * math.sin(math.radians(angle)*frequency) )  
   
  try:  
     
    while True:  
      for i in range(0, 720, 5):  
        colour( PosSinWave(50, i, 0.5),  
            PosSinWave(50, i, 1),  
            PosSinWave(50, i, 2),  
            0.1 )  
       
  except KeyboardInterrupt:  
    pass  
   
  #Stop all the PWM objects  
  RED.stop()  
  GREEN.stop()  
  BLUE.stop()  
   
  #Tidy up and remaining connections.  
  GPIO.cleanup()  
