import network
import secrets
import time
import urequests
from machine import Pin

# Set up LEDs
green_led = Pin(2, Pin.OUT)
yellow_led = Pin(3, Pin.OUT)
red_led = Pin(4, Pin.OUT)

# Set up WiFi connection
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(secrets.SSID, secrets.PASSWORD)

# Wait for the connection to establish
while not wlan.isconnected():
    time.sleep(1)

# List of websites to ping
websites = ["http://google.com", "http://amazon.com", "http://netflix.com"]

def ping_website(url):
    try:
        response = urequests.get(url)
        return response.status_code == 200
    except:
        return False

def test_connection():
    results = [ping_website(url) for url in websites]
    return results.count(True)

while True:
    successful_pings = test_connection()

    # Turn off all LEDs
    green_led.value(0)
    yellow_led.value(0)
    red_led.value(0)

    # Determine which LED to turn on
    if successful_pings == len(websites):
        # All websites responded, turn on green LED
        green_led.value(1)
    elif successful_pings > 0:
        # Some websites responded, turn on yellow LED
        yellow_led.value(1)
    else:
        # No websites responded, turn on red LED
        red_led.value(1)

    # Wait before testing again
    time.sleep(60)
