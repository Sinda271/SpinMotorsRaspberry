from gpiozero import Servo
from time import sleep

servo = Servo(2)

try:
	servo.min()
	sleep(1)
	servo.mid()
	sleep(1)
	servo.max()
	sleep(1)
	servo.min()
except Exception as e:
	print("Error: ", e)


