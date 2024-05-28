from machine import ADC, Pin, UART
import time

# Configurar el pin analógico
sensor_pin = ADC(Pin(26))

# Configurar UART
uart = UART(0, baudrate=9600, tx=Pin(12), rx=Pin(13))

def map_value(value, in_min, in_max, out_min, out_max):
    return (value - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

uart_led_count = 0  # Variable para almacenar la cantidad de LEDs encendidos

while True:
    # Leer datos UART
    if uart.any():
        uart_data = uart.read()
        uart_data_str = uart_data.decode().strip()  # Decodificar y eliminar espacios en blanco
        try:
            uart_led_count = int(uart_data_str)  # Intentar convertir la cadena a un entero
            if uart_led_count > nivel_agua:
                print("Alerta: Más LEDs encendidos de lo esperado!")
            else:
                print("Todo en orden.")
        except ValueError:  # Manejar el caso en que la cadena no sea un número entero válido
            print("Error: La cadena recibida no es un número entero válido.")
    time.sleep(1)