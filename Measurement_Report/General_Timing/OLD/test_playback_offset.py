""" Opsætning Kør alt som sudo nice -n -20

sudo nice -n -20 screen bash
    sudo nice -n -20 aplay MYFIFO
sudo nice -n -20 python3 test_playback_offset.py

"""


import RPi.GPIO as GPIO
import os

GPIO.setmode(GPIO.BOARD)
from time import sleep


def test_playback():
    GPIO.setup(37, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Input port til at starte afspillning
    have_run = 0
    # os.system("sudo nice -n -20 aplay -f S16_LE -c2 -r2000 MYFIFO")

    while True:
        Input = GPIO.input(37)
        if (Input):
            print("GPIO HIGH")
            have_run = 1
            os.system("sudo nice -n -20 cat sinus_100hz.raw > ./MYFIFO")

        elif (have_run == 1):
            os.system("^Z")
            os.system("pkill -9 -f test_playback_offset.py")
            have_run = 0


def test_playback_old():
    GPIO.setup(37, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Input port til at starte afspillning
    have_run = 0

    while True:
        Input = GPIO.input(37)
        if (Input):
            have_run = 1
            os.system("aplay -f S16_LE -c2 -r44100 firkant_16bit_stereo.raw")

        elif (have_run == 1):
            os.system("^Z")
            os.system("pkill -9 -f test_playback_offset.py")
            have_run = 0


if __name__ == "__main__":
    test_playback()

