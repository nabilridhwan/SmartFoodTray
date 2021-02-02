from microbit import *
import radio, music

radio.on()
channel = 1
radio.config(channel=channel)
tune = ["Eb6"]
buttonBCount = 0
tune1 = ["A5:1"]
tune2 = ["Gb5:1"]

(sendDone, sendCollected) = ("Done", "Collected")

def sendDoneSignal():
    music.play(tune1)
    radio.send(sendCollected)
    display.scroll("Done",50)

def sendCollectedSignal():
    music.play(tune2)
    radio.send(sendDone)
    display.scroll("Collected",50)

while True:
    if button_a.is_pressed():
        channel = channel + 1
        display.show(channel)
        # music.play(tune)

        if channel >= 20:
            channel = 1
    # Button B is pressed, it will send a done signal
    elif button_b.is_pressed():
        buttonBCount = buttonBCount + 1
    
    if buttonBCount % 2 != 0:
        sendDoneSignal()
    else:
        sendCollectedSignal()
        