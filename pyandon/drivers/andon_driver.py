from abc import ABC, abstractmethod

class AndonDriver(ABC):

    @abstractmethod
    def usb_id_supported(manufacturer_id, device_id):
        """
        Returns true if this driver supports the provider manufacturer and device IDs.

        Parameters:
            manufacturer_id - string, USB manufacturer ID
            device_id - string, USB device ID

        Returns:
            Boolean - Whether this device is supported by this driver.
        """
        pass

    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def set_light(color, pattern)
        """
        Sets the specified light to display the given pattern.

        Parameters:
            color - LightColor
            pattern - LightPattern
        """
        pass
