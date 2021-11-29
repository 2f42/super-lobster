from __future__ import annotations

import itertools

from typing import NamedTuple
from enum import Enum, unique


class Point(NamedTuple):

	x: int = 0
	y: int = 0

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

	RIGHT = 0
	DOWN = 1
	LEFT = 2
	UP = 3

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

	def __init__(self, pos=Point(), dir=Direction.RIGHT) -> Lobster:
		self.id = next(Lobster.id_iter)
		self.position = pos
		self.direction = dir

	def __repr__(self) -> str:
		return f"<Lobster {self.id} at {self.position} facing {self.direction.name}>"