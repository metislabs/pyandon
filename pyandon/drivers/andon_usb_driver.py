from abc import abstractmethod
from .andon_driver import AndonDriver
from .types import DriverType


class AndonUSBDriver(AndonDriver):

    def type(self):
        return DriverType.USB

    @abstractmethod
    def usb_id_supported(self, vendor_id, product_id):
        """
        Returns true if this driver supports the provider vendor and product IDs.

        Parameters:
            vendor_id - string, USB vendor ID
            product_id - string, USB product ID

        Returns:
            Boolean - Whether this product is supported by this driver.
        """
        pass
