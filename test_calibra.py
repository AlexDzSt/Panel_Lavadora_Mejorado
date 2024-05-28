from machine import ADC, Pin, UART
import time

# Configurar el pin analógico
sensor_pin = ADC(Pin(26))

def map_value(value, in_min, in_max, out_min, out_max):
    return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
while True:
    sensor_value = sensor_pin.read_u16()
    scaled_value = sensor_value // 64  # Dividir por 64 para obtener un rango de 0 a 1023
    nivel_agua = map_value(scaled_value, 0, 600, 0, 10)  # Mapear a nivel de agua en cm de 0 a 10 cm
    print("Nivel de agua (cm):", nivel_agua)
    time.sleep(1)