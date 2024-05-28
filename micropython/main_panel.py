from machine import UART, Pin, I2C
import actions
import alarmas
from ssd1306 import SSD1306_I2C
from time import sleep



# Configuración del UART0
uart = UART(0, baudrate=9600, tx=Pin(12), rx=Pin(13))
# Configuración de la pantalla OLED
i2c = I2C(0,scl = Pin(17), sda = Pin(16), freq = 200000)
oled = SSD1306_I2C(128, 64, i2c)

prev_data = None  # Inicializa prev_data fuera del bucle

while True:
    if uart.any():
        data = uart.read().decode('utf-8').strip()  # Elimina espacios en blanco alrededor del mensaje
        if data:
            # Mostrar mensaje de bienvenida cuando enciende el sistema
            if data == "123":
                actions.show_welcome()
            elif data == "124":
                actions.show_bye()   
            else:
                # Mostrar el ciclo seleccionado con el potenciómetro
                alarmas.play_button_beep()
                actions.read_rotary(data)
                
            if data == "IN" and prev_data:
                alarmas.play_start()
                actions.show_timer(prev_data)
                
            prev_data = data