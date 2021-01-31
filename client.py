from microbit import *
import radio
import music

radio.on()
radio.config(channel=1)
tune = ["F#6"]
tune1 = ["C4:1", "R:5"]
tune2 = ["C4:1", "R:5"]

threshold = 300

while count <= 0:
    check = radio.receive()
    display.scroll("Please Wait",100)
    if check == "done":
        display.clear()
        music.play(tune)
        display.show("Done")
        count = count + 1

while count >= 10:
check = radio.receive()
if check == "Collected":
    (readingX, readingY) = (accelerometer.get_x(), accelerometer.get_y())

    if readingX > threshold:
        display.show(Image.ARROW_W)
        music.play(tune)
    elif readingX < -threshold:
        display.show(Image.ARROW_E)
        music.play(tune)
    elif readingY > threshold:
        display.show(Image.ARROW_N)
        music.play(tune)
    elif readingY < -threshold:
        display.show(Image.ARROW_S)
        music.play(tune)
    else:
        display.show("-")
    #for i in range(0, 10):
    #    music.play(tune)
    #    display.scroll("Done",75)
    #    count = count + 1