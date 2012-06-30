#!/usr/bin/python

import time
from RPi import GPIO

# Define the connection pins
PIN_LED = 12
PIN_BUTTON = 8


def setup():
    """Setup the GPIO library / pins"""

    # Setup the connections
    GPIO.setup(PIN_LED, GPIO.OUT)
    GPIO.setup(PIN_BUTTON, GPIO.IN)

    # Reset the output LED to off
    GPIO.output(PIN_LED, False)


def main():
    """Main function"""
    
    setup()
    blink(repeat=5, sleep=0.1)
    
    GPIO.output(PIN_LED, True)
    time.sleep(1)
    GPIO.output(PIN_LED, False)

    flashes = record(duration=10, feedback=True)
    time.sleep(1)
    play(flashes)


def record(duration=5, feedback=False):
    pass


def play(flashes):
    pass


def blink(repeat=3, sleep=0.5):
    """Blink the LED the number of tmes passed in as the `repeat` argument"""

    GPIO.output(PIN_LED, False)

    i = 0
    while i < repeat:
        GPIO.output(PIN_LED, True)
        time.sleep(sleep)
        GPIO.output(PIN_LED, False)
        time.sleep(sleep)
        i += 1


if __name__ == "__main__":
    main()
