from microbit import *
import radio, music

# the channel for the radio is the tray id.
tray_id = 0
radio.on()
radio.config(channel=tray_id)
alert_tune = ["F#6"]
wordDelay = 75

tiltThreshold = 325

# Threshold
(done, collected) = ("Done", "Collected")

# Stores lasts received radio message
lastReceived = ""

while True:
    (readingX, readingY) = (accelerometer.get_x(), accelerometer.get_y())
    incoming = radio.receive()
    
    if incoming == done:
        lastReceived = done
    elif incoming == collected:
        lastReceived = collected

    if lastReceived == done:
        music.play(alert_tune)
        display.scroll("Done", delay=wordDelay)
        sleep(100)

    if readingX > tiltThreshold:
        display.show(Image.ARROW_W)
        music.play(alert_tune)
    elif readingX < -tiltThreshold:
        display.show(Image.ARROW_E)
        music.play(alert_tune)
    elif readingY > tiltThreshold:
        display.show(Image.ARROW_N)
        music.play(alert_tune)
    elif readingY < -tiltThreshold:
        display.show(Image.ARROW_S)
        music.play(alert_tune)
    else:
        display.show("-")