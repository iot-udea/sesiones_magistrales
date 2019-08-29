from picamera import PiCamera
from time import sleep

with PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.start_preview()
    sleep(5)
<<<<<<< HEAD
    camera.capture('/home/pi/Desktop/image5.jpg', use_video_port = True)
=======
    camera.capture('/home/pi/Desktop/image_ex5.jpg', use_video_port = True)
>>>>>>> master
    camera.stop_preview()
