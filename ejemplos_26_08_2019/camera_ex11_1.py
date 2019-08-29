import time
import picamera

camera = picamera.PiCamera()
try: 
  camera.resolution = (640, 480)
  camera.start_preview()
  time.sleep(1)
  num_capturas = 5
  for i, filename in enumerate(camera.capture_continuous('image{counter:02d}.jpg', use_video_port = True)):
    print('Captured image %s' % filename)
    if i == num_capturas - 1:
      break            
    time.sleep(2)
  camera.stop_preview()
except:
    camera.close()
