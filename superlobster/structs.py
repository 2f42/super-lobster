from __future__ import annotations

from typing import Dict

class Matrix:

	def __init__(self, width: int, height: int) -> None:
		self._width: int = width
		self._height: int = height
		self.__matrix: Dict[int, int] = {i: 0 for i in range(width * height)}

	@property
	def width(self) -> int:
		return self._width


	@property
	def height(self) -> int:
		return self._height

	def get(self, x: int, y: int) -> int:
		if x >= self.width or x < 0 or y >= self.height or y < 0:
			raise IndexError
		return self.__matrix[y * self.width + x]

	def set(self, x: int, y: int, value: int) -> None:
		self.__matrix[y * self.width + x] = value
