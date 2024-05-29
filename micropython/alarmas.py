from buzzer_music import music
from time import sleep
from machine import Pin

cancionON = '0 D#6 1 0;2 D#5 1 0;3 A#5 1 0;6 G#5 1 0;10 D#6 1 0;12 A#5 2 0'
cancionOFF = '0 G#6 1 0;2 D#6 1 0;4 G#5 1 0;6 A#5 1 0'
cancionFin = '0 E5 1 43;4 A5 1 43;7 A5 1 43;10 C#6 1 43;13 C#6 1 43;16 A5 1 43;19 A5 1 43;22 E6 1 43;27 E6 1 43;27 E6 1 43;32 E6 1 43;34 B6 1 43;36 A6 1 43;38 G#6 1 43;40 F#6 1 43;42 E6 1 43'
tonoBoton = '0 D#6 1 34'  
tonoInicio ='0 D5 1 34;1 A5 1 34;2 D6 1 34'     

def play_tone(cancion) -> None:
    tono = music(cancion, pins=[Pin(14)])
    for i in range(len(cancion)):
        tono.tick()
        sleep(0.04)
    tono.stop()
    
def play_on_tone() -> None:
    play_tone(cancionON)
    
def play_off_tone() -> None:
    play_tone(cancionOFF)    

def play_finish_tone() -> None:
    play_tone(cancionFin)
    
def play_button_beep() -> None:
    play_tone(tonoBoton)    
    
def play_start() -> None:
    play_tone(tonoInicio)