from gpiozero import LED
from xml.dom import minidom
from pathlib import Path

# led = LED(4)
pixels = open(str((str(Path.home())+"/pixels.xml")))
file = minidom.parse(pixels)