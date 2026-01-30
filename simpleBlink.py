from gpiozero import LED, Button
from time import sleep
from signal import pause

led = LED(17)
button = Button(26)
ledState = False
while True:
    if button.is_pressed:
        ledState = not ledState
        if ledState:
            led.on()
        else:
            led.off()
        sleep(0.3)  # Debounce delay
