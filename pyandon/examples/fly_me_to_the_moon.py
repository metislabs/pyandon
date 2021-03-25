#!/usr/bin/env python3
"""
PyAndon - Python module for interacting with a range of different andon lights

Copyright 2021, Metis Labs Ltd.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included
    in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import pyandon
import time
import sys
from pyandon import LightColor, LightPattern, BuzzerNotes


# The first two lines of Fly Me To The Moon transposed to fit
# within the range of a Patlite USB light. Implemented as a list
# of (Note, Duration) tuples.
fly_me = [
    (BuzzerNotes.A7, 1),
    (BuzzerNotes.AFLAT7, 1),
    (BuzzerNotes.GFLAT7, 1),
    (BuzzerNotes.E7, 1),
    (BuzzerNotes.D7, 1.5),
    (BuzzerNotes.E7, 0.5),
    (BuzzerNotes.GFLAT7, 1),
    (BuzzerNotes.A7, 1),
    (BuzzerNotes.AFLAT7, 1),
    (BuzzerNotes.GFLAT7, 1),
    (BuzzerNotes.E7, 1),
    (BuzzerNotes.D7, 1),
    (BuzzerNotes.DFLAT7, 3),
    (BuzzerNotes.OFF, 1),
    (BuzzerNotes.GFLAT7, 1),
    (BuzzerNotes.E7, 1),
    (BuzzerNotes.D7, 1),
    (BuzzerNotes.DFLAT7, 1),
    (BuzzerNotes.B6, 1.5),
    (BuzzerNotes.DFLAT7, 0.5),
    (BuzzerNotes.D7, 1),
    (BuzzerNotes.GFLAT7, 1),
    (BuzzerNotes.F7, 1),
    (BuzzerNotes.D7, 1),
    (BuzzerNotes.DFLAT7, 1),
    (BuzzerNotes.B6, 1),
    (BuzzerNotes.A6, 3)
]

# Beats per minute
BPM = 120

# Discover all available andon lights
devices = pyandon.find_devices()
if len(devices) == 0:
    print("No devices found")
    sys.exit(1)

# Use the first device we find
device = devices[0]
print("Found:", device.name())

# Set the lights we're going to cycle through during the song
lights = [LightColor.RED, LightColor.YELLOW, LightColor.GREEN]
light = None
i = 0

for note, duration in fly_me:
    if light is not None:
        # Switch off the light we used for the previous note
        device.set_light(light, LightPattern.OFF)
    light = lights[i]
    # Enable the next light in the sequence
    device.set_light(light, LightPattern.STATIC)
    i = i+1
    if (i > len(lights) - 1):
        # Go back to the beginning of the list of lights
        i = 0
    # Play the note
    device.set_buzzer(pyandon.BuzzerPattern.ON, [note])
    # Sleep for the length of this note
    time.sleep(duration * (60 / BPM))

# Stop the lights and buzzer on the device once we're done
device.clear()
