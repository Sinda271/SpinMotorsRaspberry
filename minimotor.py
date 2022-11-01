import time
import RPi.GPIO as GPIO

pin = 16
delay = 0.005
# Declare the GPIO settings
GPIO.setmode(GPIO.BOARD)

GPIO.setup(pin, GPIO.OUT)

while 1:

	# Set the motor speed
	GPIO.output(pin, - GPIO.HIGH) 

	time.sleep(delay)

	GPIO.output(pin, GPIO.LOW)
	time.sleep(1)
