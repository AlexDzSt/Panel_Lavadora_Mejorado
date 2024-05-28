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
    # Leer datos UART si están disponibles
    if uart.any():
        uart_data = uart.read()
        uart_data_str = uart_data.decode().strip()  # Decodificar y eliminar espacios en blanco
        print(f"Datos UART recibidos: {uart_data_str}")

        try:
            # Extraer el número desde el string, ignorando el prefijo
            uart_led_count = int(''.join(filter(str.isdigit, uart_data_str)))  # Intentar convertir la cadena a un entero
            print(f"Cantidad de LEDs después de la conversión: {uart_led_count}")  # Imprimir el valor convertido
        except ValueError:  # Manejar el caso en que la cadena no sea un número entero válido
            print("Error: La cadena recibida no es un número entero válido.")
    
    # Medir el nivel de agua
    sensor_value = sensor_pin.read_u16()
    scaled_value = sensor_value // 100
    nivel_agua = map_value(scaled_value, 0, 600, 0, 10)
    
    # Comparar el recuento de LED con el nivel de agua
    print("Nivel de agua :", nivel_agua)
    if uart_led_count < nivel_agua:
        print("Alerta: Más agua de la requerida!")
    else:
        print("Todo en orden. Nivel de agua: {} (escala 0-5)".format(nivel_agua))
    
    time.sleep(1)