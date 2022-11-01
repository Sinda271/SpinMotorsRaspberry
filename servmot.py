#from gpiozero import AngularServo
#from guizero import App, ButtonGroup, Text

#app=App(title="Servo_GUI", layout="grid")
#s = AngularServo(2, min_angle=0, max_angle=30)
# Servo Control
import RPi.GPIO as GPIO
from time import sleep
 
#servoPin = 2
#GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(servoPin, GPIO.OUT)
#pin7 = GPIO.PWM(servoPin, 50)
#pin7.start(0)
 
def angleToDutyConvert(angle):
  servoPin = 2
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(servoPin, GPIO.OUT)
  pin7 = GPIO.PWM(servoPin, 50)
  pin7.start(0)

  dutyCycle = angle / 18 + 2
  GPIO.output(servoPin, GPIO.HIGH)
  pin7.ChangeDutyCycle(dutyCycle)
  sleep(0.3)
  pin7.ChangeDutyCycle(0)

  GPIO.output(servoPin, GPIO.LOW)
  #sleep(1)
 
def sweep(degrees):
  for pos in range(0, degrees, +degrees):
    print(pos)
    angleToDutyConvert(pos)
  for pos in range(degrees, 0, -degrees):
    print(pos)
    angleToDutyConvert(pos)


#sweep(30)
