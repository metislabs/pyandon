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
    ON = 1
    PATTERN_1 = 2
    PATTERN_2 = 3
    PATTERN_3 = 4
    PATTERN_4 = 5
