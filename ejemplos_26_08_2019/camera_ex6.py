import time
import picamera

with picamera.PiCamera() as camera:
  camera.start_preview()
  camera.image_effect = 'colorswap'
  sleep(5)
  camera.capture('/home/pi/Desktop/colorswap.jpg', use_video_port = True)
  camera.stop_preview()
