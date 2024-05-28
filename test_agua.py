from machine import ADC, Pin, UART
import time

# Configurar el pin analógico
sensor_pin = ADC(Pin(26))

# Configurar UART
uart = UART(0, baudrate=9600, tx=Pin(12), rx=Pin(13))

def map_value(value, in_min, in_max, out_min, out_max):
    return (value - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

uart_led_count = 0  # Variable para almacenar la cantidad de LEDs encendidos