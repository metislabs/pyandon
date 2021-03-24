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
