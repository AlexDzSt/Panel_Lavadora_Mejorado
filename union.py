from machine import ADC, Pin, UART
import time

# Configurar el pin analógico
sensor_pin = ADC(Pin(26))

def map_value(value, in_min, in_max, out_min, out_max):
    return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

while True:
    # Leer el valor del sensor
    sensor_value = sensor_pin.read_u16()
    scaled_value = sensor_value // 100  # Escalar el valor para obtener un rango manejable
    
    # Mapear a nivel de agua en 4 niveles (0 a 3)
    nivel_agua = int(map_value(scaled_value, 0, 600, 0, 9))
    
    # Determinar el nivel de agua alcanzado
    if nivel_agua == 0:
        nivel = "Nivel 1: Bajo"
    elif nivel_agua == 1:
        nivel = "Nivel 2: Medio Bajo"
    elif nivel_agua == 2:
        nivel = "Nivel 3: Medio Alto"
    elif nivel_agua == 3:
        nivel = "Nivel 4: Alto"
    
    # Mostrar el nivel de agua alcanzado
    print("Nivel de agua alcanzado:", nivel)
    
    # Esperar 2 segundos antes de la siguiente lectura
    time.sleep(2)