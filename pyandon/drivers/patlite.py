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

import usb.util
from .andon_usb_driver import AndonUSBDriver
from .types import LightColor, BuzzerNotes


class Patlite(AndonUSBDriver):

    def __init__(self, usb_device = None):
        self.usb_device = usb_device
        if self.usb_device is not None:
            if self.usb_device.is_kernel_driver_active(0):
                self.usb_device.detach_kernel_driver(0)
            self.usb_device.set_configuration()
        self._reset()

    def _reset(self):
        self.red = 0
        self.yellow = 0
        self.green = 0
        self.blue = 0
        self.clear_light = 0
        self.tone_a = 0
        self.tone_b = 0
        self.buzzer_pattern = 0

    def name(self):
        return "Patlite USB"

    def usb_id_supported(self, vendor_id, product_id):
        return vendor_id == 0x191A and product_id == 0x8003

    def create_device(self, usb_device):
        return Patlite(usb_device)

    def set_light(self, color, pattern):
        if color == LightColor.RED:
            self.red = pattern
        elif color == LightColor.YELLOW:
            self.yellow = pattern
        elif color == LightColor.GREEN:
            self.green = pattern
        elif color == LightColor.BLUE:
            self.blue = pattern
        elif color == LightColor.CLEAR:
            self.clear_light = pattern

        self._apply()

    def set_buzzer(self, pattern, tones):
        if len(tones) > 1:
            self.tone_a = self._convert_hz(tones[0])
            self.tone_b = self._convert_hz(tones[1])
        elif len(tones) == 1:
            self.tone_a = self._convert_hz(tones[0])
        self.buzzer_pattern = pattern

        self._apply()

    def clear(self):
        # Clear lights and buzzer
        buf = (0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00)
        self.usb_device.write(1, buf, 100)
        self._reset();

    def _apply(self):
        if self.usb_device is None:
            print("Device not instantiated")
        buf = (0x00, 0x00, self.buzzer_pattern, (self.tone_a<<4) + self.tone_b, (self.red<<4) + self.yellow, (self.green<<4) + self.blue, (self.clear_light<<4), 0x00)
        self.usb_device.write(1, buf, 100)

    def _convert_hz(self, hz):
        notes = [BuzzerNotes.OFF, BuzzerNotes.A6, BuzzerNotes.BFLAT6, BuzzerNotes.B6, BuzzerNotes.C7, BuzzerNotes.DFLAT7, BuzzerNotes.D7, BuzzerNotes.EFLAT7, BuzzerNotes.E7, BuzzerNotes.F7, BuzzerNotes.GFLAT7, BuzzerNotes.G7, BuzzerNotes.AFLAT7, BuzzerNotes.A7]
        return notes.index(min(notes, key=lambda x:abs(x - hz)))

    def __del__(self):
        if self.usb_device is not None:
            usb.util.dispose_resources(self.usb_device)


def create_driver():
    return Patlite()
