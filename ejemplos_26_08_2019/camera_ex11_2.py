import time
import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (1280, 720)
    camera.start_preview()
    time.sleep(1)
    num_capturas = 5
    for i, filename in enumerate(camera.capture_continuous('image{counter:02d}.jpg', use_video_port = True)):
        print('Captured image %s' % filename)
        if i == num_capturas - 1:
            break            
        time.sleep(2)
    camera.stop_preview()
