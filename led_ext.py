#Programa que enciende el led externo
import machine
import utime

led_ext = machine.Pin(15, machine.Pin.OUT)

pause = 1

while True:
    led_ext.toggle()
    utime.sleep(pause)
    
