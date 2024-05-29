from machine import Pin, UART, I2C
from ssd1306 import SSD1306_I2C
from digital_timer import DigitalTimer
from time import sleep
import socket
import alarmas

i2c = I2C(0,scl = Pin(17), sda = Pin(16), freq = 200000)
oled = SSD1306_I2C(128, 64, i2c)
uart = UART(0, baudrate=9600, tx=Pin(12), rx=Pin(13))

wifi_data = ""
response2 = ""

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
            alarmas.play_finish_tone()
            sleep(2)
            turn_oled_off()
            break

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

def turn_oled_off() -> None:
    oled.fill(0)
    oled.show()
        
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

    
def show_cycle(ciclo: int, mensaje: str) -> None:
    send_message_to_server(mensaje)
    timer = DigitalTimer(ciclo,0)
    if response2:
        oled.fill(0)
        m, s = timer.get_time()
        time = f'Duracion: {m:02} : {s:02}'
        oled.text("Wi-Fi conectado", 0, 0)
        oled.text(mensaje, 32, 10)
        oled.text(time, 0, 20)
        paragraphs = divide_in_paragraphs(response2, 16)
        for idx, para in enumerate(paragraphs[:3]):  # Solo muestra hasta 3 párrafos
            oled.text(para, 0, 30 + idx * 10)
        oled.show()
        sleep(2)
        turn_oled_off()
    
# Funciones para interactuar con el servidor    

def test_wifi() -> None:
    import network
    ssid = 'INFINITUME850_2.4'
    password = 'liGyaaCk3B'
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while not wlan.isconnected():
        print('Waiting for connection...')
        sleep(1)
    print('Connected to Internet!')
    print('IP address:', wlan.ifconfig()[0])
    
def send_message_to_server(message):
    global response2
    host = '192.168.1.65'  # IP del servidor
    port = 12345  # Puerto del servidor

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    try:
        client_socket.sendall(message.encode())
        response = client_socket.recv(1024).decode()
        print(f"Mensaje del servidor: {response}")
        response2 = response
    except Exception as e:
        print(f"Error communicating with the server: {e}")
    finally:
        client_socket.close()

def divide_in_paragraphs(text, length):
    paragraphs = []
    for i in range(0, len(text), length):
        paragraphs.append(text[i:i+length])
    return paragraphs    
