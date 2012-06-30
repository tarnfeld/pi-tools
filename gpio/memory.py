#!/usr/bin/python

import time
from RPi import GPIO

# Define the connection pins
OUTPUT_LED = 12
INPUT_BUTTON = 8

# Setup the connections
GPIO.setup(OUTPUT_LED, GPIO.OUT)
GPIO.setup(INPUT_BUTTON, GPIO.IN)

GPIO.output(OUTPUT_LED, False)

# Main Loop
while 1:
  time.sleep(1)
  GPIO.output(OUTPUT_LED, True)
  print "On"
  time.sleep(1)
  GPIO.output(OUTPUT_LED, False)
  print "Off"
  print "Button Status:", GPIO.input(INPUT_BUTTON)

