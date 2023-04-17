from gpiozero import LED
from xml.dom import minidom
from pathlib import Path

# led = LED(4)
file = minidom.parse(str((str(Path.home())+"/pixels.xml")))
pixels = file.getElementsByTagName("pixel")

for x in pixels:
    print(x.attributes['number'].value)
    print(x.firstChild.data)