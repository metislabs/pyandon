from .andon_usb_driver import AndonUSBDriver

class Patlite(AndonUSBDriver):

    def name(self):
        return "Patlite USB"

    def usb_id_supported(self, vendor_id, product_id):
        return vendor_id == 0x191A and product_id == 0x8003

def create_driver():
    return Patlite()
