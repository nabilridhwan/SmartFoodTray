from microbit import *
import radio, music

radio.on()
channel = 1
radio.config(channel=channel)
buttonBCount = 0
(tune, tune1, tune2) = (["Eb6"], ["A5:1"], ["Gb5:1"])
wordDelay = 75
(done, collected) = ("Done", "Collected")

def sendDoneSignal():
    music.play(tune1)
    radio.send(done)
    display.scroll("Done",wordDelay)

def sendCollectedSignal():
    music.play(tune2)
    radio.send(collected)
    display.scroll("Collected",wordDelay)

while True:
    display.show(channel)

    if button_a.was_pressed():
        channel = channel + 1
        display.show(channel)
        music.play(tune)
        if channel > 20:
            channel = 1
            
    elif button_b.was_pressed():
        buttonBCount = buttonBCount + 1
        if buttonBCount % 2 != 0:
            sendDoneSignal()
        else:
            sendCollectedSignal()
    