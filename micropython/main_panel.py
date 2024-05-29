from machine import UART, Pin, I2C, ADC
import actions
import alarmas
from ssd1306 import SSD1306_I2C
from time import sleep

# Configuración del UART0
uart = UART(0, baudrate=9600, tx=Pin(12), rx=Pin(13))
# Configuración de la pantalla OLED
i2c = I2C(0,scl = Pin(17), sda = Pin(16), freq = 200000)
oled = SSD1306_I2C(128, 64, i2c)
sensor_pin = ADC(Pin(26))

prev_data = None  # Inicializa prev_data fuera del bucle

actions.test_wifi()

while True:
    if uart.any():
        data = uart.read().decode('utf-8').strip()
        if data:
            # Mostrar mensaje de bienvenida cuando enciende el sistema
            if data == "123":
                actions.show_welcome()
            # Mostrar mensaje de despedida cuando se apaga el sistema
            elif data == "124":
                actions.show_bye()   
            else:
                # Mostrar el ciclo seleccionado con el potenciómetro
                alarmas.play_button_beep()
                actions.read_rotary(data)
                
            if data == "IN" and prev_data and actions.medir_nivel_agua(sensor_pin) == True:
                alarmas.play_start()
                actions.show_timer(prev_data)
            elif data == "IN" and prev_data and actions.medir_nivel_agua(sensor_pin) == False:
                alarmas.play_error()
                actions.show_low_lvl()
                
            prev_data = data
