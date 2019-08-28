from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.start_preview()
try: 
for i in range(5):
    sleep(5)
    camera.capture('/home/pi/Desktop/image%s.jpg' % i, use_video_port = True)
camera.stop_preview()
finally:
    camera.close() 
