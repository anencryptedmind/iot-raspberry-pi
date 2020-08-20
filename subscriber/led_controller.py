import os

from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNStatusCategory
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub

import RPi.GPIO as GPIO #use GPIO from RPi.GPIO when running on actual Raspberry Pi.
#from EmulatorGUI import GPIO #use GPIO from EmulatorGUI when not running on Raspberry Pi (https://sourceforge.net/projects/pi-gpio-emulator/).

LED_PIN = 4
CHANNEL = 'led_control_channel'

GPIO.setmode (GPIO.BCM)
GPIO.setup(LED_PIN,GPIO.OUT)

pnconfig = PNConfiguration()
pnconfig.publish_key = "ADD YOUR PUBLISHER KEY HERE"
pnconfig.subscribe_key = "ADD YOUR SUBSCRIBER KEY HERE"

pubnub = PubNub(pnconfig)

class LedControlSubscribeCallback(SubscribeCallback):
  def message(self, pubnub, event):
    print("[MESSAGE received]")
    if event.message['led_state'] == 1:
      print("turning LED on!\n")
      GPIO.output(LED_PIN,True)
    else:
      print("turning LED off!\n")
      GPIO.output(LED_PIN,False)

  def presence(self, pubnub, event):
    """handle presence events"""

  def status(self, pubnub, event):
    """handle status events"""	  

pubnub.add_listener(LedControlSubscribeCallback())
pubnub.subscribe().channels(CHANNEL).execute()

print("Waiting for someone to change LED state!\n")

  
