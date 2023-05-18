import network
import urequests
import machine
import time

# Initialize Wi-Fi
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('<your SSID>', '<your password>')

# Wait for the Wi-Fi connection
while not sta_if.isconnected():
    time.sleep(1)

# Define pins for the traffic light
red_led = machine.Pin(18, machine.Pin.OUT)
green_led = machine.Pin(19, machine.Pin.OUT)

# Perform a HTTP request
def test_connection(host):
    try:
        response = urequests.get(host)
        return True
    except:
        return False

# Control the traffic light
while True:
    if test_connection('http://google.com'):
        red_led.value(0)    # Turn off the red light
        green_led.value(1)  # Turn on the green light
    else:
        green_led.value(0)  # Turn off the green light
        red_led.value(1)    # Turn on the red light

    time.sleep(60)  # Wait for a minute before testing the connection again
