#!/usr/bin/python

import time
import sys

emu = False

for arg in sys.argv:
    if arg == "emu":
        emu = True



numpixels = 144 # Number of LEDs in strip


if emu:
    import LEDStripEmu
    strip = LEDStripEmu.Strip(numpixels, 3, 144)
    # Strip(number of pixels, scale of pixels, pixels per line)
else:
    from dotstar import Adafruit_DotStar
    datapin   = 3
    clockpin  = 4
    strip     = Adafruit_DotStar(numpixels, datapin, clockpin)

    # Alternate ways of declaring strip:
    # strip   = Adafruit_DotStar(numpixels)           # Use SPI (pins 11, 12)
    # strip   = Adafruit_DotStar(numpixels, 32000000) # SPI @ ~32 MHz
    # strip   = Adafruit_DotStar()                    # SPI, No pixel buffer
    # strip   = Adafruit_DotStar(32000000)            # 32 MHz SPI, no pixel buf
    # See image-pov.py for explanation of no-pixel-buffer use.

strip.begin()            # Initialize pins for output
strip.setBrightness(64)  # Limit brightness to ~1/4 duty cycle

offset = 0
length = 15
colors = [0xFF0000, 0xFFFF00, 0x00FF00, 0x00FFFF, 0x0000FF, 0xFF00FF]

while True: # Loop forever

    offset += 1
    if offset >= numpixels:
        offset = 0

    for i in range(numpixels):
        pos = (i + offset)
        c = colors[(i/length) % len(colors)]
        strip.setPixelColor(pos % numpixels, c)
    strip.show()
    time.sleep(1.0 / 25)
