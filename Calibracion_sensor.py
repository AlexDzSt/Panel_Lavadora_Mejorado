from machine import ADC, Pin
import time

# Configurar el pin analógico
sensor_pin = ADC(Pin(26))  # GP26 es el pin A0 en la Pico W

while True:
    # Leer el valor analógico
    sensor_value = sensor_pin.read_u16()  # Lee el valor de 0 a 65535
    # Convertir a un rango de 0 a 1023 similar a Arduino si es necesario
    scaled_value = sensor_value // 64  # Dividir por 64 para obtener un rango de 0 a 1023
    print("Nivel de agua (valor analógico):", scaled_value)