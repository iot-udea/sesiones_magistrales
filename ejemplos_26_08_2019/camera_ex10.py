import time
import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (2592, 1944)
    camera.start_preview()
    time.sleep(2)
    camera.exif_tags['IFD0.Artist'] = 'Me!'
    camera.exif_tags['IFD0.Copyright'] = 'Copyright (c) 2013 Me!'
<<<<<<< HEAD
    camera.capture('foo2.jpg', use_video_port = True)
=======
    camera.capture('foo.jpg', use_video_port = True)
>>>>>>> master
    camera.stop_preview()
