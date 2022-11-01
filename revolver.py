import RPi.GPIO as GPIO
import time
import numpy as np
#from servmot import sweep

in1 = 17
in2 = 18
in3 = 27
in4 = 22

# careful lowering this, at some point you run into the mechanical limitation of how quick your motor can move
step_sleep = 0.001
X = 60

step_sequence = [[1,0,0,1],
                 [1,0,0,0],
                 [1,1,0,0],
                 [0,1,0,0],
                 [0,1,1,0],
                 [0,0,1,0],
                 [0,0,1,1],
                 [0,0,0,1]]



motor_pins = [in1,in2,in3,in4]



def cleanup():
    GPIO.output( in1, GPIO.LOW )
    GPIO.output( in2, GPIO.LOW )
    GPIO.output( in3, GPIO.LOW )
    GPIO.output( in4, GPIO.LOW )
    GPIO.cleanup()

def sign(nb):
	return int(nb/abs(nb))



def revolver(newpos):
	# setting up
	GPIO.setmode( GPIO.BCM )
	GPIO.setup( in1, GPIO.OUT )
	GPIO.setup( in2, GPIO.OUT )
	GPIO.setup( in3, GPIO.OUT )
	GPIO.setup( in4, GPIO.OUT )

	# initializing
	GPIO.output( in1, GPIO.LOW )
	GPIO.output( in2, GPIO.LOW )
	GPIO.output( in3, GPIO.LOW )
	GPIO.output( in4, GPIO.LOW )

	f = open("currentPos.txt", "r")
	current = int(f.readline())
	print("Current position: ", current)
	f.close()
	if(current == newpos):
		print("no rotation is needed")
	else:

		rot = (newpos - current)* X
		print("New position: ", newpos)
		print("Rotation angle: ", rot)
		step_count = (rot*4096)/360
		print("number of steps: ", step_count)
		motor_step_counter = 0
		try:
			i = 0
			for i in np.arange(0, abs(step_count), 1.0):
				for pin in range(0, len(motor_pins)):
					GPIO.output( motor_pins[pin], step_sequence[motor_step_counter][pin] )
				motor_step_counter = (motor_step_counter + sign(step_count)) % 8
				time.sleep( step_sleep )

		except Exception as e:
    			cleanup()
    			print("error: ", e)
		cleanup()
		print("done rotating")

		f = open("currentPos.txt", "w")
		f.write(str(newpos))
		f.close()
		#sweep(30)


#revolver(3)

