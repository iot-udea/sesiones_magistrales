import time
import picamera


with picamera.PiCamera() as camera:
  camera.start_preview()
  time.sleep(2)
  camera.capture_sequence([
   'image1.jpg',
   'image2.jpg',
   'image3.jpg',
   'image4.jpg'
  ], use_video_port=True)
  camera.stop_preview()
