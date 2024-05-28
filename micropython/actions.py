from machine import Pin, UART, I2C
from ssd1306 import SSD1306_I2C
from digital_timer import DigitalTimer
from time import sleep
import alarmas

i2c = I2C(0,scl = Pin(17), sda = Pin(16), freq = 200000)
oled = SSD1306_I2C(128, 64, i2c)
uart = UART(0, baudrate=9600, tx=Pin(12), rx=Pin(13))

def show_timer(data: str) -> None:    
    
    if data == "Ciclo delicado":
        ciclo = 30
    elif data == "Ropa blanca":
        ciclo = 45
    elif data == "Carga pesada":
        ciclo = 50
    elif data == "Lavado normal":
        ciclo = 40
    elif data == "Ciclo rapido":
        ciclo = 15
    elif data == "Ropa de color":
        ciclo = 35
        
    timer = DigitalTimer(ciclo, 0)
    
    while True:
        onoff = uart.read()
        if onoff is not None:
            onoff = onoff.decode('utf-8')
        oled.fill(0)
        m, s = timer.get_time()
        time = f'{m:02} : {s:02}'
        oled.text(data, 0, 0)
        oled.text(time, 0, 10)
        oled.show()
        timer.decrement()
        sleep(1)
        if onoff == "124":
            show_bye()
            break
        if m == 0 and s == 0:
            oled.fill(0)
            oled.text("Ciclo finalizado", 0, 10)
            oled.show()
            turn_oled_off()
            break
        
def show_cycle(ciclo: int, mensaje: str) -> None:
    timer = DigitalTimer(ciclo,0)
    oled.fill(0)
    m, s = timer.get_time()
    time = f'{m:02} : {s:02}'
    oled.text(mensaje, 0, 0)
    oled.text(time, 0, 10)
    oled.show()
    sleep(2)
    oled.fill(0)
    oled.show()

def show_welcome() -> None:
    alarmas.play_on_tone()
    oled.fill(0)
    oled.text("   Bienvenido!", 0, 30)
    oled.show()
    sleep(2)
    turn_oled_off()

def show_bye() -> None:
    alarmas.play_off_tone()
    oled.fill(0)
    oled.text("  Hasta luego", 0, 30)
    oled.show()
    sleep(2)
    turn_oled_off()
    
def show_start() -> None:
    oled.fill(0)
    oled.text("Iniciando ciclo", 0, 30)
    oled.show()
    sleep(2)
    turn_oled_off()
    
def read_rotary(data: str) -> None:
    if data == "Ciclo delicado":
        show_cycle(30, "Ciclo delicado")
    elif data == "Ropa blanca":
        show_cycle(45, "Ropa Blanca")
    elif data == "Carga pesada":
        show_cycle(50, "Carga pesada")
    elif data == "Lavado normal":
        show_cycle(40, "Lavado Normal")
    elif data == "Ciclo rapido":
        show_cycle(15, "Ciclo Rapido")
    elif data == "Ropa de color":
        show_cycle(35, "Ropa de color")

def turn_oled_off() -> None:
    oled.fill(0)
    oled.show()