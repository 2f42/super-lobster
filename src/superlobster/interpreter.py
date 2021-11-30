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

	@staticmethod
	def as_point(direction: Direction) -> Point:
		if direction is Direction.RIGHT:
			return Point(1, 0)
		elif direction is Direction.DOWN:
			return Point(0, 1)
		elif direction is Direction.LEFT:
			return Point(-1, 0)
		elif direction is Direction.UP:
			return Point(0, -1)

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
		self.position += Direction.as_point(self.direction)
