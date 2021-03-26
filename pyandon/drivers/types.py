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

from enum import Enum, IntEnum


class DriverType(Enum):
    USB = 1
    Network = 2


class LightColor(Enum):
    RED = 1
    YELLOW = 2
    GREEN = 3
    BLUE = 4
    CLEAR = 5


class LightPattern(IntEnum):
    OFF = 0
    STATIC = 1
    QUICK_FLASH = 2
    SLOW_FLASH = 3
    FLASH_FLASH_PAUSE = 4
    FLASH_PAUSE = 5


class BuzzerPattern(IntEnum):
    OFF = 0
    STATIC = 1
    PATTERN_1 = 2
    PATTERN_2 = 3
    PATTERN_3 = 4
    PATTERN_4 = 5


class BuzzerNotes(IntEnum):
    OFF = 0
    A6 = 1760
    BFLAT6 = 1865
    B6 = 1976
    C7 = 2093
    DFLAT7 = 2217
    D7 = 2349
    EFLAT7 = 2489
    E7 = 2637
    F7 = 2794
    GFLAT7 = 2960
    G7 = 3136
    AFLAT7 = 3322
    A7 = 3520
