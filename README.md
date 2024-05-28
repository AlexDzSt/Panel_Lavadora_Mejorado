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