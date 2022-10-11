import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
try:
 while 1:
  GPIO.output(10, GPIO.HIGH)
  time.sleep(0.20)
  GPIO.output(10, GPIO.LOW)
  time.sleep(0.20)
  
  GPIO.output(22, GPIO.HIGH)
  time.sleep(0.20)
  GPIO.output(22, GPIO.LOW)
  time.sleep(0.20)

  GPIO.output(24, GPIO.HIGH)
  time.sleep(0.20)
  GPIO.output(24, GPIO.LOW)
  time.sleep(0.20)

except KeyboardInterrupt:
 GPIO.cleanup()
