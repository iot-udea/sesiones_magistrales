from picamera import PiCamera
from time import sleep

camera = PiCamera()
try:
  camera.start_preview()
  sleep(5)
  camera.capture('/home/pi/Desktop/image.jpg', use_video_port = True)
  camera.stop_preview()
finally:
    camera.close() 
