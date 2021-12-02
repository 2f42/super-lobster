from __future__ import annotations

import itertools

from .geometry import Point, Direction


class Lobster:

    id_iter = itertools.count()

    def __init__(self, position=Point(), direction=Direction.EAST) -> None:
        self.id = next(Lobster.id_iter)
        self.position = position
        self.direction = direction

    def __repr__(self) -> str:
        return f"<Lobster {self.id} at {self.position} facing {self.direction.name}>"

    def step(self, steps: int = 1) -> None:
        self.position += Point.from_direction(self.direction) * steps

    def turn(self, steps: int) -> None:
        self.direction += steps
