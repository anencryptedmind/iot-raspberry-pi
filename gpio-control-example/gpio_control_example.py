import RPi.GPIO as GPIO #use GPIO from RPi.GPIO when running on actual Raspberry Pi.
#from EmulatorGUI import GPIO #use GPIO from EmulatorGUI when not running on Raspberry Pi (https://sourceforge.net/projects/pi-gpio-emulator/).

import time

GPIO.setmode (GPIO.BCM)
PIN = 4

GPIO.setup(PIN,GPIO.OUT)

while True:
  GPIO.output(PIN,True)
  time.sleep(1)
  GPIO.output(PIN,False)
  time.sleep(1)
