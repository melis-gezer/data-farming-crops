"""Corn crop module."""


class Corn:
    """Represents a corn crop."""

    def __init__(self):
        """Initialize corn with zero grains."""
        self.grains = 0

    def water(self):
        """Increase grains by 10 when watered."""
        self.grains += 10

    def ripe(self):
        """Return True if grains are at least 15."""
        return self.grains >= 15
    