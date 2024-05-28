from machine import ADC, Pin
import time

# Configurar el pin analógico
sensor_pin = ADC(Pin(26))  # GP26 es el pin A0 en la Pico W

while True:
    # Leer el valor analógico