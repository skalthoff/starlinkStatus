# Internet Connectivity Monitor with Raspberry Pi Pico W

This repository contains code to create a simple device that uses a Raspberry Pi Pico W to monitor whether it can connect to the Internet. 

## Hardware Requirements

- Raspberry Pi Pico W
- 3 LEDs (Red, Yellow, Green)
- 3 x 330 Ohm resistors
- Breadboard
- Jumper wires

## Wiring Instructions

1. Connect the anode (longer leg) of the Green LED to GPIO pin 2 on the Raspberry Pi Pico W. Connect the cathode (shorter leg) to a 330-ohm resistor, and then connect the other end of the resistor to a ground pin on the Raspberry Pi Pico W.
2. Repeat step 1 for the Yellow LED and Red LED, connecting them to GPIO pins 3 and 4 respectively.
3. Ensure that your Raspberry Pi Pico W is connected to your computer via a USB cable.

Please note that these GPIO pins are just examples; you can use any available GPIO pins on the Raspberry Pi Pico W. Adjust the code to reflect the GPIO pins you are using.

## Software Setup

1. Install MicroPython on your Raspberry Pi Pico W. You can follow [this guide](https://www.raspberrypi.org/documentation/rp2040/getting-started/#getting-started-with-micropython) from the official Raspberry Pi documentation to do this.
2. Clone this repository to your local machine: `git clone https://github.com/YourUsername/YourRepository.git`
3. Open the `secrets.py` file in the cloned repository and replace `"your_wifi_ssid"` and `"your_wifi_password"` with your actual WiFi credentials.
4. Upload the `secrets.py` and `main.py` files to your Raspberry Pi Pico W. You can do this by copying and pasting the code into the Thonny Python IDE and saving it to the Pico W, or by using a tool like `ampy` or `rshell`.

## How It Works

The `main.py` script will ping a list of websites every 60 seconds. If all websites respond, it will light up the Green LED. If some but not all websites respond, it will light up the Yellow LED. If no websites respond, it will light up the Red LED. 

The list of websites to ping is defined in the `websites` variable in the `main.py` script. You can modify this list to include any websites you want.

## Troubleshooting

If you are having trouble getting the script to run, make sure that:

- Your WiFi credentials in the `secrets.py` file are correct.
- The GPIO pins in the `main.py` script match the GPIO pins you connected your LEDs to.
- Your Raspberry Pi Pico W is properly connected to your computer and powered on.
- You have installed MicroPython on your Raspberry Pi Pico W.

If you are still having trouble, feel free to open an issue in this repository or reach out to me directly.