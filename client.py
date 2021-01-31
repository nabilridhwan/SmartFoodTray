from microbit import *
import radio, music

# the channel for the radio is the tray id.
tray_id = 1
radio.on()
radio.config(channel=tray_id)
alert_tune = ["F#6"]

threshold = 300

doneRadioReceive = 'd'
collectedRadioReceive = 'c'

while True
check = radio.receive()

if check is doneRadioReceive:
    display.clear()
    for i in range(0, 10):
        music.play(alert_tune)
        display.scroll("Done",75)

if check is collectedRadioReceive:
    (readingX, readingY) = (accelerometer.get_x(), accelerometer.get_y())

    if readingX > threshold:
        display.show(Image.ARROW_W)
        music.play(alert_tune)
    elif readingX < -threshold:
        display.show(Image.ARROW_E)
        music.play(alert_tune)
    elif readingY > threshold:
        display.show(Image.ARROW_N)
        music.play(alert_tune)
    elif readingY < -threshold:
        display.show(Image.ARROW_S)
        music.play(alert_tune)
    else:
        display.show("-")