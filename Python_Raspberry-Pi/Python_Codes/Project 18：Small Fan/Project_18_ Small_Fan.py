from machine import Pin
import time

#Pin of each section of L293D and set as output 
IN1_Pin = 17
IN2_Pin = 16
ENA_Pin = 18 #Control the speed of the motor

# speed：speed，0-100
# direction: Rotation direction,1 is clockwise,0 stops,-1 counterclockwise
# speed_pin：Pin number that controls the start and stop of the motor
def motorRun(speed, direction, speed_pin, clockwise_pin, anti_clockwise_pin):
    if speed > 100: speed=100
    if speed < 0: speed=0
    in1 = machine.Pin(anti_clockwise_pin, machine.Pin.OUT)
    in2 = machine.Pin(clockwise_pin, machine.Pin.OUT)
    pwm = machine.PWM(machine.Pin(speed_pin))
    pwm.freq(50)
    pwm.duty_u16(int(speed/100*65535))
    if direction < 0:
        in2.value(0)
        in1.value(1)
    if direction == 0:
        in2.value(0)
        in1.value(0)
    if direction > 0:
        in2.value(1)
        in1.value(0)

while True:
    motorRun(100, 1, ENA_Pin, IN2_Pin, IN1_Pin)
    time.sleep(5)
    motorRun(100, 0, ENA_Pin, IN2_Pin, IN1_Pin)
    time.sleep(2)
    motorRun(80, -1, ENA_Pin, IN2_Pin, IN1_Pin)
    time.sleep(5)
    motorRun(100, 0, ENA_Pin, IN2_Pin, IN1_Pin)
    time.sleep(2)