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
        # Realizar comparación con los datos del sensor de agua
        sensor_value = sensor_pin.read_u16()
        scaled_value = sensor_value // 100
        nivel_agua = map_value(scaled_value, 0, 650, 0, 10)
        uart_led_count = int(uart_data)
        if uart_led_count > nivel_agua:
            print("Alerta: Más LEDs encendidos de lo esperado!")
        else:
            print("Todo en orden.")
    time.sleep(1)