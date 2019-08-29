import time
import picamera

with picamera.PiCamera() as camera:
  camera.start_preview()
  camera.image_effect = 'colorswap'
<<<<<<< HEAD
  time.sleep(5)
=======
  sleep(5)
>>>>>>> master
  camera.capture('/home/pi/Desktop/colorswap.jpg', use_video_port = True)
  camera.stop_preview()
