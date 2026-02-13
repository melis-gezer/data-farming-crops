# pylint: disable=too-few-public-methods

"""Base crop module."""


class Crop:
    """Represents a generic crop."""

    def __init__(self):
        """Initialize crop with zero grains."""
        self.grains = 0

    def ripe(self):
        """Return True if grains are at least 15."""
        return self.grains >= 15
    