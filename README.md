# Microcontroller Network for Simulating a Washing Machine Control Panel

This project represents a network of interconnected microcontrollers designed to simulate the control panel of a modern washing machine. At its core, this system replicates the primary user interface and operational functionalities found in typical washing machines, providing a comprehensive and realistic simulation environment.
This code implements a versatile system that not only simulates the control panel of a washing machine but also provides user interaction and real-time data communication. It ensures precise water level measurement and intuitive control through both auditory and visual feedback mechanisms.

<br>

**Key Features:**


_Buzzer with Specific Sounds:_

Each interaction with the control panel triggers a unique sound, providing auditory feedback to the user.


_Water Level Sensor:_

An analog sensor simulates a real washing machine tank by measuring the water level. The sensor is connected to the analog pin of the microcontroller, reading and scaling the data to obtain standarized value.


_WiFi Connectivity:_

Utilizing the WiFi functionality of the Raspberry Pi Pico W, the system connects to a server to log data for each washing cycle. This allows real-time updates and monitoring of the server information.


_UART Communication:_

The system can receive data via UART to compare the measured water level with an external reference, such as the selection function guiding by LEDs illuminated. If the water level exceeds this reference, an alert is triggered.

<br>

**Additional Functionalities:**


_Rotary LED Display_

The system includes a rotary LED display consisting of seven segments, which can be controlled by an analog input, in this case a potentiometer. Adjusting the potentiometer influences the segments' illumination, creating various patterns.

<br>

**Required Components**:

Microcontroller Board (2): - A microcontroller board Raspberry Pi Pico and a Raspberry Pi Pico W.

7-Segment LED display (1): - A seven-segment LED display module.

Potentiometer (1): - A linear potentiometer with a resistance value suitable for your microcontroller's analog input range (e.g., 10kΩ).

Resistors (17): - 17 resistors (220 Ohms) for current limiting on the LEDs.

Jumper Wires: - A set of jumper wires for connecting components.

Breadboards (2): - A breadboard can be helpful for prototyping and experimenting with the circuit.

LED (1).

Push Buttons (3): - Buttons for selection, pause/resume, and system power control.

OLED Display i2c (128x64) (1): Device used to display the status of the machine.

Water Detector / Sensor (1): Device used to measure the water level on a glass.

10 Segment LED Bar Graph Display (1): Used to select a water level on the panel.


<br>
<br>
