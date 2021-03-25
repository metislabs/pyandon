import usb.util
from .andon_usb_driver import AndonUSBDriver
from .types import LightColor


class Patlite(AndonUSBDriver):

    def __init__(self, usb_device = None):
        self.usb_device = usb_device
        if self.usb_device is not None:
            if self.usb_device.is_kernel_driver_active(0):
                self.usb_device.detach_kernel_driver(0)
            self.usb_device.set_configuration()
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
            self.tone_a = tones[0]
            self.tone_b = tones[1]
        elif len(tones) == 1:
            self.tone_a = tones[0]
        self.buzzer_pattern = pattern

        self._apply()

    def clear(self):
        # Clear lights
        buf = (0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00)
        self.usb_device.write(1, buf, 100)

    def _apply(self):
        if self.usb_device is None:
            print("Device not instantiated")
        buf = (0x00, 0x00, self.buzzer_pattern, (self.tone_a<<4) + self.tone_b, (self.red<<4) + self.yellow, (self.green<<4) + self.blue, (self.clear_light<<4), 0x00)
        self.usb_device.write(1, buf, 100)


def create_driver():
    return Patlite()
