from picamera import PiCamera
from time import sleep

with PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.start_preview()
    sleep(5)
    camera.capture('/home/pi/Desktop/image_ex5.jpg')
    camera.stop_preview()
