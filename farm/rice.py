"""Rice crop module."""

from farm.crop import Crop


class Rice(Crop):
    """Represents a rice crop."""

    def water(self):
        """Increase grains by 5 when watered."""
        self.grains += 5

    def transplant(self):
        """Increase grains by 10 when transplanted."""
        self.grains += 10
        