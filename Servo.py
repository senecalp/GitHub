
from machine import Pin, PWM
from time import sleep

# Set up PWM Pin for servo control
servo_pin = machine.Pin(15)
servo = PWM(servo_pin)

# Set Duty Cycle for Different Angles
max_duty = 10000
min_duty = 1

#Set PWM frequency
frequency = 50
servo.freq (frequency)

# Set up sensor Pin
sensor_pin = 14
sensor = Pin(sensor_pin, Pin.IN)

try:
    while True:
        if sensor.value() == 0:
            #Servo at 0 degrees
            servo.duty_u16(min_duty)
            sleep(2)

            #Servo at 180 degrees
            servo.duty_u16(max_duty)
            sleep(2)    
      
except KeyboardInterrupt:
    print("Keyboard interrupt")
    # Turn off PWM 
    servo.deinit()
