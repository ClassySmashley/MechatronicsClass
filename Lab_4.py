import RPi.GPIO as GPIO
import time

#Set board mode for gpio pins
GPIO.setmode(GPIO.BCM)

# LED on test
R1 = 17

GPIO.setup(R1, GPIO.OUT)

try:
  while 1:
    GPIO.output(R1, GPIO.HIGH)
except KeyboardInterupt:
  GPIO.cleanup()
