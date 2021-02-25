import RPi.GPIO as GPIO
import time

#Set board mode for gpio pins
GPIO.setmode(GPIO.BCM)

# LED on test
R1 = 4
R2 = 17
R3 = 27
G = 22
Y1 = 5
Y2 = 6
Y3 = 13
#Set difficulty
easy = 0.5
normal = 0.25
hard = 0.1
diff = easy

GPIO.setup(R1, GPIO.OUT)
GPIO.setup(R2, GPIO.OUT)
GPIO.setup(R3, GPIO.OUT)
GPIO.setup(G, GPIO.OUT)
GPIO.setup(Y1, GPIO.OUT)
GPIO.setup(Y2, GPIO.OUT)
GPIO.setup(Y3, GPIO.OUT)
GPIO.add_event_detect(19, GPIO.RISING)

try:
  while 1:
    GPIO.output(R1, GPIO.HIGH)
    time.sleep(diff)
    GPIO.output(R1, GPIO.LOW)
    GPIO.output(R2, GPIO.HIGH)
    time.sleep(diff)
    GPIO.output(R2, GPIO.LOW)
    GPIO.output(R3, GPIO.HIGH)
    time.sleep(diff)
    GPIO.output(R3, GPIO.LOW)
    GPIO.output(G, GPIO.HIGH)
    time.sleep(diff)
    GPIO.output(G, GPIO.LOW)
    GPIO.output(Y1, GPIO.HIGH)
    time.sleep(diff)
    GPIO.output(Y1, GPIO.LOW)
    GPIO.output(Y2, GPIO.HIGH)
    time.sleep(diff)
    GPIO.output(Y2, GPIO.LOW)
    GPIO.output(Y3, GPIO.HIGH)
    time.sleep(diff)
    GPIO.output(Y3, GPIO.LOW)
    if GPIO.event_detected(19):
      break
    
except KeyboardInterrupt:
  GPIO.cleanup()
