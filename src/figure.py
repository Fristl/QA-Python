"""Module with base figure class."""

from abc import ABC
from abc import abstractmethod

from common.exceptions import FigureError
from common.exceptions import SizeError
from common.typings import Number
from common.typings import SquareUnit


class Figure(ABC):
    """Abstract base figure class."""

    @classmethod
    def check_size(cls, size: Number) -> Number:
        """Validate input size during initialization."""
        if size > 0:
            return size
        raise SizeError(size)

    @abstractmethod
    def _area(self) -> SquareUnit:
        """Calculate the area of the figure."""

    def get_area(self) -> SquareUnit:
        """Return the area of the figure."""
        return self._area()

    @abstractmethod
    def _perimeter(self) -> Number:
        """Calculate the perimeter of the figure."""

    def get_perimeter(self) -> Number:
        """Return the perimeter of the figure."""
        return self._perimeter()

    def add_area(self, figure: "Figure") -> SquareUnit:
        """Summary the area of self figure and another figure."""
        if isinstance(figure, Figure):
            return self.get_area() + figure.get_area()
        raise FigureError(figure)

