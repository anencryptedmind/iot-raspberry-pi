# iot-raspberry-pi
Control LED connected to raspberry pi remotely (over the internet) using PubNub APIs.

A simple example showing how to control raspberry pi GPIO pins remotely using publish-subscribe pattern.

Prerequisites:
1. Install Python (https://www.python.org/).
2. Install pubnub library (Run command -> 'pip install pubnub').
3. If you don't have a raspberry pi device then download GPIO emulator (https://sourceforge.net/projects/pi-gpio-emulator/).
4. Create PubNub account and demo keys for use (https://www.pubnub.com/).

If you are going to use GPIO emulator then skip steps #1 to #3.

Steps:
1. Connect anode of LED to GPIO 4 (Refer diagram https://www.raspberrypi.org/documentation/usage/gpio/README.md).
2. Connect cathode of LED to a ~200 to ~300 ohm resistor.
3. Connect the other end of resistor to any of the Ground pins (Refer diagram https://www.raspberrypi.org/documentation/usage/gpio/README.md).
4. If you are going to use GPIO emulator then open gpio_control_example.py and led_controller.py, and comment or uncomment the necessary GPIO import statements (Refer code            comments).
4. Run gpio_control_example.py to verify that you are able to control the connected LED locally (Run command -> 'python gpio_control_example.py').
5. Add your pubisher and subscriber keys to led_controller.py and led_control_portal.html
6. Run led_controller.py on raspberry pi (Run command -> 'led_controller.py').
7. Open led_control_portal.html in your phone browser or any other place you would like to and contol the LED remotely (over the internet) using on/off buttons (you should also be    able to see logs on raspberry pi).

Now that you are able to control a LED remotely, go ahead and try out anything else you would like to control by controlling raspberry pi GPIO pins!




