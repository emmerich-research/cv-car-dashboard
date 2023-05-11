from gpiozero import Buzzer
from time import sleep

buzzer = Buzzer(5)

def beep():
    buzzer.beep()
    sleep(0.05)
    buzzer.off()
