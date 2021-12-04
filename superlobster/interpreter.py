from __future__ import annotations

import itertools

from .geometry import Point, Direction, Domain, ClosedDomain


class Lobster:

    id_iter = itertools.count()

    def __init__(self, position=Point(), direction=Direction.EAST, domain=Domain(), pointer=Point()) -> None:
        self.id = next(Lobster.id_iter)
        self.position = domain.transform(position)
        self.direction = direction
        self.domain = domain
        self.stack = []
        self.pointer = domain.transform(pointer)

    def __repr__(self) -> str:
        return f"<Lobster {self.id} at {self.position} facing {self.direction.name} in {self.domain}>"

    def step(self, steps: int = 1) -> None:
        new_pos = self.position + Point.from_direction(self.direction) * steps
        self.position = self.domain.transform(new_pos)

    def turn(self, steps: int) -> None:
        self.direction += steps

    def clone(self, where=None, facing=None) -> Lobster:
        if where is None:
            where = self.direction + 1  # on the current lobster's right
        if facing is None:
            facing = self.direction
        new_pos = self.position + Point.from_direction(where)
        return self.__class__(new_pos, facing, self.domain)

    def push(self, value: int) -> None:
        value = value & 255
        self.stack.append(value)

    def pop(self) -> int:
        return self.stack.pop()

    def peek(self) -> int:
        return self.stack[-1]

    def shift_pointer(self, offset: Point) -> Point:
        new_pos = self.pointer + offset
        self.pointer = self.domain.transform(new_pos)
        return self.pointer
