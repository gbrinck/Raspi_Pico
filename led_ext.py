#Programa que enciende el led externo
import machine
import utime

led_ext = machine.Pin(15, machine.Pin.OUT)
pause = 100000
while True:
    led_ext.value(not led_ext())
    utime.sleep_us(pause)
    