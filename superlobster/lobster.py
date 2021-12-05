from __future__ import annotations

import itertools

from .geometry import Point, Direction, Domain
from enum import Enum, unique, auto


@unique
class LobsterState(Enum):

    DOING = auto()
    READ = auto()
    PSYCHIC = auto()
    DONE = auto()
    HALT = auto()


class Lobster:

    id_iter = itertools.count()

    def __init__(self, position=Point(), direction=Direction.EAST, domain=Domain(), pointer=Point()) -> None:
        self.id = next(Lobster.id_iter)
        self.position: Point = domain.transform(position)
        self.direction: Direction = direction
        self.domain: Domain = domain
        self.state: LobsterState = LobsterState.DONE
        self.left_claw: int = 0
        self.right_claw: int = 0
        self.brain: int = 0
        self.pointer: Point = domain.transform(pointer)

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

    def left_swap(self) -> None:
        self.brain, self.left_claw = self.left_claw, self.brain

    def right_swap(self) -> None:
        self.brain, self.right_claw = self.right_claw, self.brain

    def add(self) -> int:
        self.brain = self.left_claw + self.right_claw
        return self.brain

    def sub(self) -> int:
        self.brain = self.left_claw - self.right_claw
        return self.brain

    def mul(self) -> int:
        self.brain = self.left_claw * self.right_claw
        return self.brain

    def div(self) -> int:
        self.brain = self.left_claw // self.right_claw
        return self.brain

    def shift_pointer(self, offset: Point) -> Point:
        new_pos = self.pointer + offset
        self.pointer = self.domain.transform(new_pos)
        return self.pointer
