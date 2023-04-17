from gpiozero import LED
import xmltodict

led = LED(4)
file = open("~/pixels.xml", "r")

