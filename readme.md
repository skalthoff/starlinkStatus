# Starlink Internet Connection Indicator

This is a simple device built with a Raspberry Pi Pico W that indicates whether the Starlink dish has an internet connection. The device uses a traffic light-style indicator (LEDs) for visual feedback.

## Requirements

- Raspberry Pi Pico W
- Micro-USB cable
- Traffic light-style indicator (3 LEDs: red, yellow, green)
- Resistor pack
- Breadboard and jumper wires
- Wi-Fi with internet access

## Setup

1. **Install Thonny IDE**: Thonny IDE is used to program the Raspberry Pi Pico using MicroPython. You can download it from https://thonny.org. Follow the installation procedure with all default settings.

2. **Flash MicroPython Firmware on Raspberry Pi Pico W**:

   - Connect the Raspberry Pi Pico to your computer while holding the BOTSET button at the same time to enter bootloader mode.
   - Open Thonny IDE.
   - Go to Tools > Options.
   - Select the Interpreter tab on the new window that opens.
   - Select MicroPython (Raspberry Pi Pico) for the interpreter, and the Try to detect port automatically for the Port.
   - Click on Install or update MicroPython.
   - Select the MicroPython variant accordingly to the board you’re using (Pico W in this case).
   - Click Install.

3. **Circuit Setup**: Connect the LEDs to the GPIO pins of the Raspberry Pi Pico W using the resistor pack and jumper wires. Make sure to connect the LEDs to the 3.3V power and ground.

4. **Code Setup**: Upload the MicroPython code to the Raspberry Pi Pico W via the Thonny IDE. Replace `<your SSID>` and `<your password>` in the code with your Wi-Fi credentials.

   ```python
   import network
   import time

   # Initialize Wi-Fi
   sta_if = network.WLAN(network.STA_IF)
   sta_if.active(True)
   sta_if.connect('<your SSID>', '<your password>')

   # Wait for the Wi-Fi connection
   while not sta_if.isconnected():
       time.sleep(1)

   # Perform a ping test
   def ping_test(host):
       # Code to ping `host` and return True if successful, False otherwise
       pass

   # Control the traffic light
   if ping_test('google.com'):
       # Code to turn on the green light
   else:
       # Code to turn on the red light
   ```

   Please note that the `ping_test` function and the code to control the traffic light are not provided, as they depend on the specific libraries and hardware you are using. For the traffic light, you might use LEDs connected to the GPIOs, and for the `ping_test` function, you might need a library that provides a ping functionality.

## Running

Once the setup is complete, the device should start working automatically. The green LED will turn on if the Starlink dish has an internet connection. Otherwise, the red LED will turn on.

## Troubleshooting

If you encounter issues, please check the following:

- The LEDs are correctly connected to the GPIO pins, power, and ground.
- The Wi-Fi credentials in the code are correct.
- The Raspberry Pi Pico W is correctly flashed with the MicroPython firmware.
- The `ping_test` function is correctly implemented.

## Contributing

Please feel free to contribute to this project. Any contributions you make are greatly appreciated.

## License

This project is licensed under the MIT License.

Please let me know if you have any other questions.