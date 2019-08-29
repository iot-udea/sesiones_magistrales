from picamera import PiCamera
from time import sleep

with PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.start_preview()
    sleep(5)
    camera.capture('/home/pi/Desktop/image5.jpg', use_video_port = True)
    camera.stop_preview()
