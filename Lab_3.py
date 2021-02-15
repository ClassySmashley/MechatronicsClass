import RPI.GPIO as GPIO
import time

#Set board mode for gpio pins
GPIO.setmode(GPIO.BCM)

One = 14
Two = 15
Three = 18
Four = 23
Five = 24
Six = 25
Seven = 8
Eight = 7
Button = 9

#Setup board pin numbers
GPIO.setup(One, GPIO.OUT) #1st LED
GPIO.setup(Two, GPIO.OUT) #2nd LED
GPIO.setup(Three, GPIO.OUT) #3rd LEd
GPIO.setup(Four, GPIO.OUT) #4th LED
GPIO.setup(Five, GPIO.OUT) #5th LED
GPIO.setup(Six, GPIO.OUT) #6th LED
GPIO.setup(Seven, GPIO.OUT) #7th LED
GPIO.setup(Eight, GPIO.OUT) #8th LED
GPIO.setup(Button, pull_up_down=PUD
