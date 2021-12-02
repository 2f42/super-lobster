from __future__ import annotations

from dataclasses import dataclass, astuple
from enum import Enum, unique


@unique
class Direction(Enum):

    EAST = 0
    SOUTH = 1
    WEST = 2
    NORTH = 3

    def __add__(self, other: int) -> Direction:
        if isinstance(other, int):
            return Direction((self.value + other) % 4)
        return NotImplemented

    def __sub__(self, other: int) -> Direction:
        if isinstance(other, int):
            return Direction((self.value - other) % 4)
        return NotImplemented


@dataclass(frozen=True, eq=True)
class Point:

    x: int = 0
    y: int = 0

    @classmethod
    def from_direction(cls, direction: Direction) -> Point:
        if direction is Direction.EAST:
            return cls(1, 0)
        elif direction is Direction.SOUTH:
            return cls(0, 1)
        elif direction is Direction.WEST:
            return cls(-1, 0)
        elif direction is Direction.NORTH:
            return cls(0, -1)

    def __add__(self, other: object) -> Point:
        if isinstance(other, Point):
            _x, _y = astuple(self)
            x, y = astuple(other)
            return Point(_x + x, _y + y)
        return NotImplemented

    def __sub__(self, other: object) -> Point:
        if isinstance(other, Point):
            _x, _y = astuple(self)
            x, y = astuple(other)
            return Point(_x - x, _y - y)
        return NotImplemented

    def __mul__(self, other: object) -> Point:
        if isinstance(other, int):
            _x, _y = astuple(self)
            return Point(_x * other, _y * other)
        if isinstance(other, Point):
            _x, _y = astuple(self)
            x, y = astuple(other)
            return Point(_x * x, _y * y)
        return NotImplemented


@dataclass(frozen=True)
class Domain:

    def transform(self, point: Point) -> Point:
        return point


@dataclass(frozen=True)
class ClosedDomain(Domain):

    width: int
    height: int

    def transform(self, point: Point) -> Point:
        return Point(point.x % self.width, point.y % self.height)
