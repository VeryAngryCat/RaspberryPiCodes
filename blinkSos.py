from gpiozero import LED, Button
from time import sleep

led = LED(17)
button = Button(26)
dot = 0.2
dah = dot * 3
rest = dot
word_rest = dot * 7

def blink(duration):
  led.on()
  sleep(duration)
  led.off()
  sleep(rest)

def sos():
  for _ in range(3):
    blink(dot)
  for _ in range(3):
    blink(dah)
  for _ in range(3):
    blink(dot)
  sleep(word_rest)

while True:
    button.wait_for_press()
    sos()
