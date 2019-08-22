import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try: 
  while True:
    input_state = GPIO.input(18)
    if input_state == False:
      print('Button Pressed')
      time.sleep(0.2)
    else:
      print('Button Released')
      time.sleep(0.2)
finally:
  print("Cleaning Up!")
  GPIO.cleanup()
	
