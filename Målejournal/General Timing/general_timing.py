import threading
import RPi.GPIO as GPIO
import os
import time, threading

# sudo nice -n -20 python3 ./general_timing.py

GPIO.setmode(GPIO.BOARD)
input_pin = 37
output_pin = 40
global ledState

GPIO.setup(input_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Input port til at starte afspillning
GPIO.setup(output_pin, GPIO.OUT)
GPIO.output(output_pin, 0)


def buttonEventHandler_rising(pin):
    # turn LED on
    # GPIO.output(LED_output,True)
    GPIO.output(output_pin, not GPIO.input(output_pin))
    #raise Exception('button pressed')


GPIO.add_event_detect(input_pin, GPIO.RISING, callback=buttonEventHandler_rising)

try:
    while True: pass
except:
    GPIO.cleanup()

if __name__ == "__main__":
    buttonEventHandler_rising()
