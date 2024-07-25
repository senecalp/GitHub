
from machine import Pin, PWM
from time import sleep

# Set up PWM Pin for servo control
servo_pin = machine.Pin(15)
servo = PWM(servo_pin)

# Set Duty Cycle for Different Angles
max_duty = 7500
min_duty = 1
half_duty = 4200

#Set PWM frequency
frequency = 50
servo.freq (frequency)

try:
    while True:
        if sensor.value() == 0:
            #Servo at 0 degrees
            servo.duty_u16(min_duty)
            sleep(2)
            #Servo at 90 degrees
            servo.duty_u16(half_duty)
            sleep(2)
            #Servo at 180 degrees
            servo.duty_u16(max_duty)
            sleep(2)    
      
except KeyboardInterrupt:
    print("Keyboard interrupt")
    # Turn off PWM 
    servo.deinit()
