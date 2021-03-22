from abc import ABC, abstractmethod

class AndonDriver(ABC):

    @abstractmethod
    def name(self):
        pass

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

    @abstractmethod
    def set_light(self, color, pattern):
        """
        Sets the specified light to display the given pattern.

        Parameters:
            color - LightColor
            pattern - LightPattern
        """
        pass
