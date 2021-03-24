from .andon_usb_driver import AndonUSBDriver
from .types import LightColor

class Patlite(AndonUSBDriver):

    def __init__(self, usb_device = None):
        self.usb_device = usb_device
        self.red = 0
        self.yellow = 0
        self.green = 0
        self.blue = 0
        self.clear = 0
        self.tone_a = 0
        self.tone_b = 0

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
        elif color == LightColor.CLEAR:
            self.clear = pattern

        self._apply_lights()

    def _apply_lights(self):
        buf = (0x00, 0x00, 0x08, 0xff, (self.red<<4) + self.yellow, (self.green<<4) + self.blue, (self.clear<<4), 0x00)
        print(buf)


def create_driver():
    return Patlite()
