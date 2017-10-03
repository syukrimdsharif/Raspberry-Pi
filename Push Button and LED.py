import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.IN, GPIO.PUD_UP)

try:
    while True:
        if GPIO.input(24) == 0:
            GPIO.output(23, GPIO.HIGH)
        else:
            GPIO.output(23, GPIO.LOW)

except KeyboardInterrupt:
    GPIO.cleanup()
