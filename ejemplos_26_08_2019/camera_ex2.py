from picamera import PiCamera
from time import sleep

with picamera.PiCamera() as camera:
    camera.start_preview()
    time.sleep(10)
    camera.stop_preview()
