from __future__ import annotations

import itertools

from typing import NamedTuple
from enum import Enum, unique


class Point(NamedTuple):

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
			_x, _y = self
			x, y = other
			return Point(_x + x, _y + y)
		return NotImplemented

	def __sub__(self, other: object) -> Point:
		if isinstance(other, Point):
			_x, _y = self
			x, y = other
			return Point(_x - x, _y - y)
		return NotImplemented


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


class Lobster:

	id_iter = itertools.count()

	def __init__(self, position=Point(), direction=Direction.RIGHT) -> Lobster:
		self.id = next(Lobster.id_iter)
		self.position = position
		self.direction = direction

	def __repr__(self) -> str:
		return f"<Lobster {self.id} at {self.position} facing {self.direction.name}>"

	def step(self) -> None:
		self.position += Point.from_direction(self.direction)
