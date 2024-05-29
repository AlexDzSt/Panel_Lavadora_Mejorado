# Microcontroller Network for Simulating a Washing Machine Control Panel

![Untitled Diagram drawio (2)](https://github.com/AlexDzSt/Panel_Lavadora_Mejorado/assets/141947909/60fa7890-bd14-472c-9208-3974c7bdeddd)

<br>

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

# General Implementation Description

This project involves the implementation of a microcontroller-based system that simulates a washing machine control panel, leveraging various components and functionalities such as LEDs, buttons, a rotary LED display, an OLED screen, UART communication, Wi-Fi connectivity, and a server-client architecture.

**Microcontroller Setup and Peripherals Initialization:**

*LEDs and Buttons:*

Multiple LEDs are used to indicate the status of different operations (e.g., power, selection, pause).
Buttons are configured with pull-up resistors for detecting user inputs, such as powering on/off, selecting a washing cycle, and pausing/resuming operations.

*Rotary LED Display:*

A rotary LED display is controlled using GPIO pins and an ADC to read values from a potentiometer. The display shows different patterns based on the analog input.

*OLED Display:*

An I2C-based OLED screen displays various messages and the current status of the washing machine cycles, such as a welcome message, selected cycle, timer, and completion message.

**Communication Interfaces:**

*UART Communication:*

UART is used for serial communication between the microcontroller and external devices. Messages related to washing cycles are sent and received through the UART interface.

*Wi-Fi Connectivity:*

The system connects to a Wi-Fi network to send and receive data from a server, enabling remote monitoring and control of the washing machine cycles.

*Control Logic:*

Main Control Loop: The main control loop continuously reads the states of the buttons and updates the system status accordingly. It handles the selection of washing cycles, pausing and resuming operations, and triggering the rotary LED display.

Rotary LED Logic: Based on the potentiometer reading, the system determines which segments of the rotary LED display to light up and sends corresponding messages over UART.

Timer and Cycle Management: A digital timer is used to manage the duration of each washing cycle. The remaining time is displayed on the OLED screen, and specific tones are played at the start and end of cycles.

**Server-Client Architecture:**

*Server Implementation:* A server script listens for incoming TCP connections. Upon receiving a message (representing a selected washing cycle), it processes the message to generate a detailed description of the cycle and sends this response back to the client.

*Client-Side Actions:* On the client side, the microcontroller sends messages to the server and displays the received response on the OLED screen. This allows the system to provide detailed information about each washing cycle to the user.

By integrating these components and functionalities, the project effectively simulates the control panel of a washing machine, providing a comprehensive and interactive user experience. The combination of local control (via buttons and rotary LED display) and remote monitoring (via UART and Wi-Fi communication) showcases the versatility and capability of the microcontroller-based system.

<br>

# Description of the code

**Rotary LED Library (crotaryled.c/crotaryled.h)**

This library provides a comprehensive set of functions for controlling a rotary LED display, reading analog input from a potentiometer, and using UART for communication. It enables precise control of LED states and facilitates interaction with external devices through serial communication.

**Purpose:** Provides functions for controlling the rotary LED display and handling UART communication for washing machine cycle selection.

*PINS_SIZE*: Defines the constant size of the pins array.

*pins*: Declares a static array of uint32_t to store the digital pin assignments for the rotary LED display.

*rl_mask*: Declares a static uint32_t variable to hold the bit mask representing the active LED(s).

*rl_delay*: Defines the constant delay (in milliseconds) between reading the potentiometer and updating the LED (not defined in the given code, but typically would be).

*ANALOG_PIN*: Defines the GPIO pin used for analog input (potentiometer).

*UART_ID*: Defines the UART port used for communication.

*BAUD_RATE*: Defines the baud rate for UART communication.

*UART_TX_PIN*: Defines the GPIO pin used for UART transmission.

*UART_RX_PIN*: Defines the GPIO pin used for UART reception.

*rl_construct(const int a[])*: Initializes the pins array with the provided pin assignments.

*rl_init()*: Initializes the digital pins for the rotary LED as outputs, initializes the analog pin for potentiometer reading, and sets up UART communication.

*rl_read_value()*: Reads the analog value from the potentiometer and converts it to a bit mask representing the active LED(s) based on predefined threshold levels.

*rl_turn_led_on()*: Turns on the LED(s) determined by the rl_mask value.

*rl_clear()*: Turns off all LEDs in the rotary display.

*rotary_led()*: Calls rl_read_value to determine the active LED(s), turns them on, delays briefly, and then turns them off. Additionally, it sends UART messages corresponding to different washing machine cycles based on the active LED(s).

<br>

**Peripheral Control Library (peripherals.c/peripherals.h)**

This library provides essential functions for initializing and controlling various peripherals, including LEDs, buttons, and a 14-segment display. It allows for the efficient management of GPIO pins and offers simple interfaces for toggling LEDs, reading button states, and driving complex display segments.

**Purpose**: Provides functions for initializing and controlling LEDs, buttons, and a 14-segment display.

init_led(int pin): Initializes the specified GPIO pin for LED output.

encender_led(int pin): Toggles the state of the specified LED pin.

apagar_led(int pin): Turns off the LED connected to the specified pin.

init_boton(int pin): Initializes the specified GPIO pin for button input and enables the internal pull-up resistor.

leer_boton_OnOff(int boton_OnOff, int led_OnOff): Reads the state of the On/Off button and controls the associated LED. It returns true if the button is pressed, otherwise false.

init_display(int primer_gpio): Initializes the GPIO pins for a 7-segment display starting from the specified GPIO pin.

turn_display_on(int bits[], int val, int primer_gpio): Turns on the segments of a 7-segment display to represent the given value. The bits array contains the bit patterns for each digit.

clear_display(int bits[], int val, int primer_gpio): Turns off all segments of a 7-segment display.

<br>

**Pin Definitions (pin_list.h)**

This file provides a centralized location for all pin assignments, making the code more readable and easier to maintain. By defining these constants, changes to pin assignments can be made in one place without needing to update multiple parts of the code.

**Purpose**: Provides constant definitions for the pin assignments used in the washing machine control panel project, including pins for LEDs, switches, analog inputs, and UART communication.

*Rotary LED Display Pins*: These pins are assigned to the segments of the rotary LED display, enabling control of each segment individually.

*Analog Input Pin*: This pin is used to read analog signals, typically from a potentiometer, to control the rotary LED display.

*Switch Pins*: These pins are assigned to the various switches on the control panel, allowing the microcontroller to detect user inputs for on/off, cycle selection, and pause/resume.

*LED Pins*: This pin is assigned to an LED that indicates whether the system is turned on or off.

*UART Pins*: These pins are used for UART communication, allowing the microcontroller to send and receive data to/from other devices or systems.

<br>

**Main Control Program (main.c)**

Purpose: Implements the main control logic for simulating a washing machine control panel, including the initialization and handling of LEDs, buttons, a rotary LED display, and UART communication.

This main control program is designed to simulate the control panel of a washing machine, handling user inputs via buttons and providing feedback through LEDs and a rotary LED display. It also includes UART communication for additional control and monitoring capabilities.

<br>

**Actions Library (actions.py)**

This file integrates various peripherals to simulate the functionality of a washing machine control panel, making it a core part of the project's user interface and control logic.

**Purpose**: Provides functions to control and interact with various peripherals and functionalities of the washing machine simulation system, including an OLED display, UART communication, and Wi-Fi connectivity.

**Function Definitions:**

*show_timer(data: str) -> None*: Displays the timer on the OLED based on the selected wash cycle and updates the display every second. Handles the end of the cycle and user interruptions.

*show_welcome() -> None*: Displays a welcome message on the OLED and plays the on tone.

*show_bye() -> None*: Displays a goodbye message on the OLED and plays the off tone.

*show_start() -> None*: Displays a starting cycle message on the OLED.

*turn_oled_off() -> None*: Clears the OLED display.

*read_rotary(data: str) -> None*: Reads the selected cycle from the rotary input and displays the corresponding cycle information.

*show_cycle(ciclo: int, mensaje: str) -> None*: Displays the cycle duration and message on the OLED, sends the message to the server, and handles the server response.

**Server Interaction Functions:**

*test_wifi() -> None*: Connects to a specified Wi-Fi network and prints the IP address once connected.

*send_message_to_server(message)*: Sends a message to a specified server and stores the response.

*divide_in_paragraphs(text, length)*: Divides a given text into paragraphs of specified length for display purposes.

<br>

**Main Panel Script (main_panel.py)**

This script forms the core of the washing machine control panel, enabling user interaction through UART commands, displaying relevant information on the OLED screen, and managing the overall system state.

**Purpose**: This script integrates the main functionalities of the washing machine control panel. It manages UART communication, OLED display interactions, and triggers specific actions based on received UART messages.

**Functionality:**

*UART and OLED Initialization*: The UART is initialized with specified baud rate, TX, and RX pins. The OLED display is initialized using I2C communication.

*Wi-Fi Test*: The script tests the Wi-Fi connection using *actions.test_wifi()*.

*Main Loop*: The main loop continuously checks for incoming data via UART. If data is received, it is decoded and stripped of any surrounding whitespace.

*Data Handling*:

The received data is stored in prev_data to manage the cycle selection and start functionality.

<br>

**Server Script (server.py)**

Run the script to start the server, the server listens on the specified IP and port, processes incoming messages, and sends appropriate responses based on the message content. The server continues to run indefinitely, handling each connection in sequence.

**Purpose**: This script sets up a TCP server to process messages related to washing machine cycles. It listens for incoming connections, processes the received messages, and returns appropriate responses based on the message content.

**Functions and Variables**:

*process_message(message)*: This function takes a message string as input and returns a corresponding response based on predefined washing machine cycles.

*start_server()*: This function sets up the server, listens for incoming connections, and handles message reception and response sending.

**Functionality:**

*process_message(message)*: Maps specific cycle names to their descriptions. Returns the appropriate description for each cycle or a default message if the cycle is not recognized.

*start_server()*:

Configures the server with a specified IP address and port, initializes a socket for TCP communication, binds the socket to the given host and port, listens for incoming connections and processes them in an infinite loop. For each connection, it receives a message from the client, processes the message using *process_message()*, sends the processed response back to the client, handles exceptions that may occur during communication, and closes the client connection after processing.

<br>
<br>

# Required Components

To implement this project using the specified devices, follow the steps below to configure and connect each component, and then integrate them with the provided code:

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

Water sensor diagram

![image](https://github.com/AlexDzSt/Panel_Lavadora_Mejorado/assets/141947909/5f2d896f-8b46-4eb0-9ec7-dc80141d18c3)

RotaryLed diagram

![image](https://github.com/AlexDzSt/Panel_Lavadora_Mejorado/assets/141947909/3df4691a-98b7-4583-a4ff-2b8ff341b6db)


<br>
<br>

# Conclusion

The project involves creating a simulated washing machine control panel using a network of microcontrollers, primarily focusing on Raspberry Pi Pico and Pico W boards. The implementation includes various components such as a 7-segment LED display, potentiometer, resistors, LEDs, push buttons, an OLED display, a water detector/sensor, and a 10-segment LED bar graph display.

This implementation ensures a comprehensive and interactive control system for a simulated washing machine, demonstrating the integration of multiple components and technologies for an effective user interface and functionality.
