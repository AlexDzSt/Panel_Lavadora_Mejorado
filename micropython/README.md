Panel de lavadora
Este proyecto utiliza un microcontrolador Raspberry Pi Pico para controlar una lavadora inteligente. El sistema incluye una pantalla OLED para mostrar información del ciclo de lavado, un temporizador digital para controlar el tiempo del ciclo, y un módulo de alarma para reproducir sonidos.

Características
Selección de ciclos de lavado predefinidos (Ciclo delicado, Ropa blanca, Carga pesada, Lavado normal, Ciclo rápido, Ropa de color)
Pantalla OLED para mostrar el tiempo restante del ciclo y el tipo de ciclo seleccionado
Temporizador digital para controlar el tiempo del ciclo de lavado
Módulo de alarma para reproducir sonidos de inicio y finalización del ciclo
Comunicación UART para recibir señales de encendido/apagado desde un dispositivo externo

Requisitos
Raspberry Pi Pico
Pantalla OLED SSD1306 (128x64 píxeles)
Buzzer pasivo 3v
Cable USB para programar el Raspberry Pi Pico

Instalación
Conecta los siguientes pines del Raspberry Pi Pico:
I2C: SCL (Pin 17), SDA (Pin 16)
UART: TX (Pin 12), RX (Pin 13)
Conecta la pantalla OLED al bus I2C.
Conecta el buzzer pasivo al Pin 14
Carga el código del proyecto en el Raspberry Pi Pico utilizando MicroPython.

Uso
Al encender el sistema, se mostrará un mensaje de bienvenida en la pantalla OLED y se reproducirá un sonido de inicio.
El usuario puede seleccionar un ciclo de lavado utilizando un dispositivo externo que envíe una señal UART con el nombre del ciclo (por ejemplo, "Ciclo delicado", "Ropa blanca", etc.).
Una vez seleccionado el ciclo, se mostrará el tiempo restante del ciclo en la pantalla OLED y comenzará la cuenta regresiva.
Cuando el ciclo finalice, se mostrará un mensaje en la pantalla OLED y se reproducirá un sonido de finalización
Para apagar el sistema, el dispositivo externo debe enviar la señal UART "124"