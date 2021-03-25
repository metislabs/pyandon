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

from abc import ABC, abstractmethod


class AndonDriver(ABC):

    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def type(self):
        "Returns the type of driver this is."
        pass

    @abstractmethod
    def set_light(self, color, pattern):
        """
        Sets the specified light to display the given pattern.

        Parameters:
            color - LightColor
            pattern - LightPattern
        """
        pass

    @abstractmethod
    def set_buzzer(self, pattern, tones):
        """
        Sets the buzzer.

        Parameters:
            pattern - BuzzerPattern
            tones - List of BuzzerTone
        """
        pass

    @abstractmethod
    def clear(self):
        """
        Clears all lights and buzzers.
        """
        pass
