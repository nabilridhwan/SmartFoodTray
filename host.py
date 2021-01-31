from microbit import *
import radio
import music

channel = 1
radio.on()
radio.config(channel=channel)
tune = ["Eb6"]
tune1 = ["A5:1"]
tune2 = ["Gb5:1"]

while True:
    if button_a.is_pressed():
        channel = channel + 1
        display.show(channel)
        music.play(tune)
        if channel >= 20:
            channel = 1
    if button_b.is_pressed():
        music.play(tune1)
        radio.send("Done")
        display.scroll("Done",50)
    if button_b.is_pressed() and button_a.is_pressed():
        music.play(tune2)
        radio.send("Collected")
        display.scroll("Collected",50)