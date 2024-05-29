# Microcontroller Network for Simulating a Washing Machine Control Panel

This project represents a network of interconnected microcontrollers designed to simulate the control panel of a modern washing machine. At its core, this system replicates the primary user interface and operational functionalities found in typical washing machines, providing a comprehensive and realistic simulation environment.
This code implements a versatile system that not only simulates the control panel of a washing machine but also provides user interaction and real-time data communication. It ensures precise water level measurement and intuitive control through both auditory and visual feedback mechanisms.

**Key Features:**


_Buzzer with Specific Sounds:_

Each interaction with the control panel triggers a unique sound, providing auditory feedback to the user.


_Water Level Sensor:_

An analog sensor simulates a real washing machine tank by measuring the water level. The sensor is connected to the analog pin of the microcontroller, reading and scaling the data to obtain standarized value.


_WiFi Connectivity:_

Utilizing the WiFi functionality of the Raspberry Pi Pico W, the system connects to a server to log data for each washing cycle. This allows real-time updates and monitoring of the server information.


_UART Communication:_

The system can receive data via UART to compare the measured water level with an external reference, such as the selection function guiding by LEDs illuminated. If the water level exceeds this reference, an alert is triggered.


**Additional Functionalities:**


_Rotary LED Display_

The system includes a rotary LED display consisting of seven segments, which can be controlled by an analog input, in this case a potentiometer. Adjusting the potentiometer influences the segments' illumination, creating various patterns.
