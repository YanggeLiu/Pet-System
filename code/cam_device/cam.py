#from imutils.video import VideoStream
import threading
import cv2
import time
from picamera import PiCamera
from picamera.array import PiRGBArray
import RPi.GPIO as GPIO

outputFrame = None
lock = threading.Lock()
'''
cap = cv2.VideoCapture(0)
cap.set(3,320)
cap.set(4,200)
cap.set(5,24)
'''


def vision_mode(status):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(4, GPIO.OUT)
    if status == '0':
        GPIO.output(4, GPIO.LOW)
    else:
        GPIO.output(4, GPIO.HIGH)


def detect_motion():
    '''
    global cap, outputFrame,lock
    while True:
        ret, frame = cap.read()
        with lock:
            outputFrame = frame.copy()
    '''
    global outputFrame, lock
    camera = PiCamera()
    camera.resolution = (320, 200)
    camera.framerate = 32
    rawCapture = PiRGBArray(camera, size=(320, 200))

    time.sleep(1)

    for frame in camera.capture_continuous(rawCapture, format='bgr', use_video_port=True):
        image = frame.array
        outputFrame = image

        rawCapture.truncate(0)


def generate():
    global outputFrame, lock
    while True:
        with lock:
            if outputFrame is None:
                continue
            flag, encodedImage = cv2.imencode(".jpg", outputFrame)

            if not flag:
                continue
        yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' +
              bytearray(encodedImage) + b'\r\n')
