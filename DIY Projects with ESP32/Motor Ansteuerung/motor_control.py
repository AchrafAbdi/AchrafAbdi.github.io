from machine import Pin, PWM
import time

# ================================
# DC motor with ESP32 + MOSFET
# Run 5 sec, stop 3 sec, repeat
# ================================

motor_pin = Pin(18, Pin.OUT)
motor_pwm = PWM(motor_pin, freq=20000, duty_u16=0)

def set_speed(percent):
    if percent < 0:
        percent = 0

    if percent > 100:
        percent = 100

    duty_value = int((percent / 100) * 65535)
    motor_pwm.duty_u16(duty_value)

while True:
    set_speed(60)      # motor runs at 60%
    print("Motor ON")
    time.sleep(5)

    set_speed(0)       # motor stops
    print("Motor OFF")
    time.sleep(3)