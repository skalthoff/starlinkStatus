# Internet Connectivity Checker using Raspberry Pi Pico W

This project uses a Raspberry Pi Pico W to check if your Starlink dish has internet connectivity. The status of the internet connectivity is indicated via a traffic-light-style indicator (two LEDs).

## Hardware Required

- Raspberry Pi Pico W
- Green LED
- Red LED
- 2 x 220 Ohm resistors
- Breadboard
- Jumper wires

## Hardware Setup

1. Connect the longer leg (anode) of the red LED to pin 18 of the Pico W through a 220 Ohm resistor, and the shorter leg (cathode) to a ground (GND) pin.
2. Connect the longer leg of the green LED to pin 19 of the Pico W through another 220 Ohm resistor, and the shorter leg to another ground (GND) pin.

## Software Setup

1. Install Thonny IDE on your computer. You can download it from this link: https://thonny.org/.
2. Connect the Raspberry Pi Pico W to your computer via a micro USB cable. Hold the BOOTSEL button on the Pico W while connecting it to enter bootloader mode.
3. Open Thonny IDE, and go to Tools > Options. In the Interpreter tab, select MicroPython (Raspberry Pi Pico) for the interpreter, and select Try to detect port automatically for the Port. Click on Install or update MicroPython.
4. After the MicroPython firmware is installed, you can write and upload the code to the Pico W. Open the `main.py` file from this project in Thonny IDE, replace `<your SSID>` and `<your password>` in the file with your Wi-Fi SSID and password, and then save it to the Pico W.

## Running the Program

After you have uploaded the `main.py` file to the Pico W, the program will start automatically whenever the Pico W is powered up. 

The green LED will light up if the Starlink dish has internet connectivity, and the red LED will light up if the dish is not connected to the internet. The program will check the internet connectivity every minute and update the LED status accordingly.