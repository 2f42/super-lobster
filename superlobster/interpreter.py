from __future__ import annotations

import itertools

from .geometry import Point, Direction, Domain, ClosedDomain


class Lobster:

    id_iter = itertools.count()

    def __init__(self, position=Point(), direction=Direction.EAST, domain=Domain()) -> None:
        self.id = next(Lobster.id_iter)
        self.position = domain.transform(position)
        self.direction = direction
        self.domain = domain

    def __repr__(self) -> str:
        return f"<Lobster {self.id} at {self.position} facing {self.direction.name} in {self.domain}>"

    def step(self, steps: int = 1) -> None:
        new_pos = self.position + Point.from_direction(self.direction) * steps
        self.position = self.domain.transform(new_pos)

    def turn(self, steps: int) -> None:
        self.direction += steps
