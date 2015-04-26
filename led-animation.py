#!/usr/bin/python

# Simple strand test for Adafruit Dot Star RGB LED strip.
# This is a basic diagnostic tool, NOT a graphics demo...helps confirm
# correct wiring and tests each pixel's ability to display red, green
# and blue and to forward data down the line.  By limiting the number
# and color of LEDs, it's reasonably safe to power a couple meters off
# USB.  DON'T try that with other code!

import time
from dotstar import Adafruit_DotStar

numpixels = 144 # Number of LEDs in strip

# Here's how to control the strip from any two GPIO pins:
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

# Runs 10 LEDs at a time along strip, cycling through red, green and blue.
# This requires about 200 mA for all the 'on' pixels + 1 mA per 'off' pixel.

offset = 0
length = 15
total_length = 20
color = 0xFF00000        # 'On' color (starts red)
colors = [0xFF0000, 0xFFFF00, 0x00FF00, 0x00FFFF, 0x0000FF, 0xFF00FF]
colorshift = 0

while True:                              # Loop forever

    offset += 1
    if offset >= numpixels:
        offset = 0

    for i in range(numpixels):
        pos = (i + offset)
        c = colors[(i/length) % len(colors)]
        strip.setPixelColor(pos % numpixels, c)
    strip.show()
    time.sleep(1.0 / 25)




    # for offset in range(length):
    #     for i in range(offset, numpixels + total_length, total_length):
    #         strip.setPixelColor(i, color)
    #         strip.setPixelColor(i - length, 0)
    #     strip.show()                     # Refresh strip
    #     time.sleep(1.0 / 25)

    # if cur_pos > total_length:   # Restarting drawing the dashes from their start
    #     cur_pos = 0
    #     colorshift = 0
    # else:
    #     cur_pos += 1
        # colorshift += 24 // (length + 1)

    # color = color if color else 0xFF00000
    time.sleep(1.0 / 25)             # Pause 20 milliseconds (~50 fps)


    # for i in range(cur_pos - (total_length + offset), numpixels + total_length, total_length):
    #     strip.setPixelColor(i + offset, color) # Turn on 'head' pixel
    #     strip.setPixelColor(i - length + offset, 0)     # Turn off 'tail'
    # strip.show()                     # Refresh strip
    # time.sleep(1.0 / 25)             # Pause 20 milliseconds (~50 fps)
    #
    # cur_pos += 1                        # Advance head position
    # if(cur_pos >= total_length - 1):           # Off end of strip?
    #     cur_pos    = 1              # Reset to start
    #     color >>= 8              # Red->green->blue->black
    #     if(color == 0): color = 0xFF0000 # If black, reset to red
    #     offset += 1
    #     if(offset >= total_length):
    #         offset = 0
