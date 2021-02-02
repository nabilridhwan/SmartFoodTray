from microbit import *
import radio, music

# the channel for the radio is the tray id.
tray_id = 1
radio.on()
radio.config(channel=tray_id)
alert_tune = ["F#6"]

tiltThreshold = 300

(receiveDone, receiveCollected) = ("Done", "Collected")

lastReceived = ""

while True:
    (readingX, readingY) = (accelerometer.get_x(), accelerometer.get_y())
    incoming = radio.receive()
    
    if incoming == receiveDone:
        display.clear()
        lastReceived = receiveDone
    #     music.play(alert_tune)
    #     display.scroll("Done", delay=75)
    #     sleep(100)
    elif incoming == receiveCollected:
        lastReceived = receiveCollected
    #     display.clear()
    #     display.scroll("Collected",delay=75)

    # itemIsDone = incoming == receiveDone
        
    # while itemIsDone:
        # music.play(alert_tune)
        # display.scroll("Done", delay=75)
        # sleep(100)
    
    if lastReceived == receiveDone:
        music.play(alert_tune)
        display.scroll("Done", delay=75)
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