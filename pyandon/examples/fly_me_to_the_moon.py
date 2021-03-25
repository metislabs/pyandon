#!/usr/bin/env python3
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
