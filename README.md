# Panel_Lavadora_Mejorado

Este proyecto utiliza un microcontrolador para medir el nivel de agua utilizando un sensor analógico y comunica el estado a través de UART. El código está escrito en MicroPython y es compatible con microcontroladores como el Raspberry Pi Pico.

## Descripción

El sistema mide el nivel de agua a través de un sensor conectado al pin analógico del microcontrolador. Los datos se leen y se escalan para obtener un valor en centímetros. Además, el sistema puede recibir datos a través de UART para comparar el nivel de agua medido con una referencia externa (por ejemplo, la cantidad de LEDs encendidos). Si el nivel de agua excede esta referencia, se emite una alerta.

## Hardware Necesario

- Microcontrolador (Raspberry Pi Pico)
- Sensor de nivel de agua conectado al pin analógico (GP26 en el Pico)
- Conexiones UART (TX en pin 12, RX en pin 13)
- Conexión a una fuente de alimentación adecuada (3.3v)

## Conexiones

- **Sensor de nivel de agua:**
  - VCC a 3.3V
  - GND a GND
  - Salida analógica a GP26

- **UART:**
  - TX del microcontrolador a RX del dispositivo UART (pin 12)
  - RX del microcontrolador a TX del dispositivo UART (pin 13)

## Instalación
    
1. **Configurar el entorno MicroPython:**
   - Siga las instrucciones para instalar MicroPython en su microcontrolador [aquí](https://micropython.org/download/rp2-pico/).

2. **Subir el código al microcontrolador:**
   - Conecte su microcontrolador a su computadora.
   - Use un IDE como Thonny para copiar y pegar el código en un nuevo archivo y guárdelo como `main.py` en su microcontrolador.
3. **Alambrar el sistema>**
   - Alambrar la Pico w asi como el sensor de agua -tierra -voltaje y -datos
   - Si se requiere alambrar tambien los puertos UART para la resepcion y envio de datos.(seguir el esquema [Sensor_Agua.jpg](https://github.com/AlexDzSt/Panel_Lavadora_Mejorado/blob/Noe/Sensor_Agua.jpg)) 

## Código

```python
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
        print(f"Datos UART recibidos: {uart_data_str}")  # Imprimir los datos UART recibidos
        
        try:
            uart_led_count = int(uart_data_str)  # Intentar convertir la cadena a un entero
            print(f"Cantidad de LEDs después de la conversión: {uart_led_count}")  # Imprimir el valor convertido
        except ValueError:
            print("Error: La cadena recibida no es un número entero válido.")
    
    # Medir el nivel de agua
    sensor_value = sensor_pin.read_u16()
    scaled_value = sensor_value // 100
    nivel_agua = map_value(scaled_value, 0, 600, 0, 10)
    
    # Comparar el recuento de LED con el nivel de agua
    print("Nivel de agua:", nivel_agua)
    if uart_led_count < nivel_agua:
        print("Alerta: Más agua de la requerida!")
    else:
        print("Todo en orden. Nivel de agua: {} (escala 0-5)".format(nivel_agua))
    
    time.sleep(1)
```

## Uso

- **Conectar el hardware:**

    - Asegúrese de que todas las conexiones estén correctas según la sección de conexiones.

- **Iniciar el sistema:**

    - Conecte el microcontrolador a la fuente de alimentación.
    - El sistema comenzará a medir el nivel de agua y a leer los datos de UART automáticamente.

- **Monitorizar la salida:**

    - Observe los mensajes impresos en la consola serie para ver el nivel de agua y las alertas.

## Contribuciones
Las contribuciones son bienvenidas. Por favor, envíe un pull request o abra un issue para discutir cualquier cambio que desee realizar.