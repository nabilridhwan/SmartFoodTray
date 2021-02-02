from microbit import *
import radio, music

radio.on()
channel = 1
radio.config(channel=channel)
tune = ["Eb6"]
# tune1 = ["A5:1"]
# tune2 = ["Gb5:1"]

doneRadioSend = 'd'
collectedRadioSend = 'c'

while True:
    if button_a.is_pressed():
        channel = channel + 1
        display.show(channel)
        # music.play(tune)

        if channel >= 20:
            channel = 1

    # Button B is pressed, it will send a done signal
    elif button_b.is_pressed():
        # music.play(tune1)
        radio.send(doneRadioSend)
        display.scroll("Done",50)

    elif button_b.is_pressed() and button_a.is_pressed():
        music.play(tune2)
        radio.send(doneRadioReceive)
        display.scroll("Collected",50)