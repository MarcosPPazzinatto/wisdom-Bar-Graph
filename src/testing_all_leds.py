from machine import PWM
from machine import Pin
import time

led_25   = Pin(13, Pin.OUT)
led_50   = Pin(4, Pin.OUT)
led_75   = Pin(16, Pin.OUT)
led_100  = Pin(17, Pin.OUT)

led_25.off()
led_50.off()
led_75.off()
led_100.off()

#Author: 'Marcos P Pazzinatto'
#Description: 'Testing All LEDs'

while True:
  led_25.off()
  led_50.off()
  led_75.off()
  led_100.off()
  time.sleep(2)
  led_25.on()
  led_50.on()
  led_75.on()
  led_100.on()
  time.sleep(1)
