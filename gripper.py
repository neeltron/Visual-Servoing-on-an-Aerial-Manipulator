import RPi.GPIO as GPIO
from time import sleep
import pi_servo_hat

in1 = 24
in2 = 23
temp1=1

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")

def open_arm(duration):
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    sleep(duration)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)


def close_arm(duration):
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    sleep(duration)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)

test = pi_servo_hat.PiServoHat()
test.restart()

test.move_servo_position(0, 45)
test.move_servo_position(1, 45)

open_arm(4)
sleep(1)

test.move_servo_position(0, 90)
test.move_servo_position(1, 90)

close_arm(4)
