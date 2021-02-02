from microbit import *
import radio, music

# the channel for the radio is the tray id.
tray_id = 1
radio.on()
radio.config(channel=tray_id)
alert_tune = ["F#6"]

tiltThreshold = 300

(receiveDone, receiveCollected) = ("Done", "Collected")
isDone = False

while True:
    (readingX, readingY) = (accelerometer.get_x(), accelerometer.get_y())
    incoming = radio.receive()
    
    if incoming == receiveDone:
        isDone = True
    elif incoming == receiveCollected:
        isDone = False
        
    while isDone:
        display.clear()
        music.play(alert_tune)
        display.scroll("Done", 75)

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