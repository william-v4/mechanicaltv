from gpiozero import LED
from xml.dom import minidom
from pathlib import Path
from time import sleep
led = LED(5)
# ir receiver on pin 17rps
file = minidom.parse(str((str(Path.home())+"/pixels.xml")))
pixels = file.getElementsByTagName("pixel")
rps = 20
delay = 60 / rps

for x in pixels:
    print(x.attributes['number'].value)
    print(x.firstChild.data)

while True:
    for x in pixels:
        if x.attributes['number'].value == "True":
            led.on()
        else:
            led.off()
        sleep(rps)