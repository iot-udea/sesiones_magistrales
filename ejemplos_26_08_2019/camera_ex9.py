from picamera import PiCamera
from time import sleep

with PiCamera() as pycam:
    pycam.start_preview()
    for effect in camera.IMAGE_EFFECTS:
       camera.image_effect = effect
       camera.annotate_text = "Effect: %s" % effect
       sleep(5)
    pycam.stop_preview()