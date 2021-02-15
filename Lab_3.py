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
GPIO.setup(Button, GPIO.IN, pull_up_down=GPIP.PUD_DOWN)

count = 0
while 1:
  if GPIO.input(Button): #Button press
    count = count + 1 #increase count
    GPIO.output(One, GPIO.HIGH) #Turn on LED
  if GPIO.input(Button):
    count = count + 1
    GPIO.output(Two, GPIO.HIGH)
  if GPIO.input(Button): #Button press
    count = count + 1 #increase count
    GPIO.output(Three, GPIO.HIGH) #Turn on LED
  if GPIO.input(Button): #Button press
    count = count + 1 #increase count
    GPIO.output(Four, GPIO.HIGH) #Turn on LED
  if GPIO.input(Button): #Button press
    count = count + 1 #increase count
    GPIO.output(Five, GPIO.HIGH) #Turn on LED
  if GPIO.input(Button): #Button press
    count = count + 1 #increase count
    GPIO.output(Six, GPIO.HIGH) #Turn on LED
  if GPIO.input(Button): #Button press
    count = count + 1 #increase count
    GPIO.output(Seven, GPIO.HIGH) #Turn on LED
  if GPIO.input(Button): #Button press
    count = count + 1 #increase count
    GPIO.output(Eight, GPIO.HIGH) #Turn on LED
  if count == 8:
    if GPIO.input(Button): #turn off all LEDs
      count = 0
      GPIO.output(One, GPIO.LOW)
      GPIO.output(Two, GPIO.LOW)
      GPIO.output(Three, GPIO.LOW)
      GPIO.output(Four, GPIO.LOW)
      GPIO.output(Five, GPIO.LOW)
      GPIO.output(Six, GPIO.LOW)
      GPIO.output(Seven, GPIO.LOW)
      GPIO.output(Eight, GPIO.LOW)
except KeyboardInterupt: #ctrl + C ends loop
  GPIO.cleanup()
    
