import time
import RPi.GPIO as GPIO

# Set up GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)
GPIO.setup(18, GPIO.IN)
GPIO.setup(21, GPIO.OUT)

# Read values from the soil moisture sensors
moisture_value_1 = GPIO.input(17)
moisture_value_2 = GPIO.input(18)

# Determine whether to water or not
if moisture_value_1 == 0 and moisture_value_2 == 1:
    print("Irrigation not required")
    GPIO.output(21, GPIO.LOW)
elif moisture_value_1 == 1 and moisture_value_2 == 1:
    print("Irrigation required")
    time.sleep(2)
    print("Turning the motors ON")
    time.sleep(1)
    GPIO.output(21, GPIO.HIGH)
    print("Irrigating now")
    time.sleep(5)
    print("Turning the motors OFF")
    time.sleep(1)
    GPIO.output(21, GPIO.LOW)
else:
    print("Irrigation not required")
    GPIO.output(21, GPIO.LOW)
