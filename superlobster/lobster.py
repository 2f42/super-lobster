from __future__ import annotations
from typing import Generator

import itertools

from .geometry import Point, Direction, Domain
from enum import Enum, unique, auto


@unique
class LobsterState(Enum):

    HALT = auto()    # no longer running
    DONE = auto()    # ready for next step
    FETCH = auto()   # read from current position
    READ = auto()    # read from pointer
    MODIFY = auto()  # write to current position
    WRITE = auto()   # write to pointer
    CLONE = auto()   # lobster cloning go brrr


class Lobster:

    id_iter = itertools.count()

    def __init__(self, position=Point(), direction=Direction.EAST, domain=Domain(), pointer=Point()) -> None:
        self.id = next(Lobster.id_iter)
        self.position: Point = domain.transform(position)
        self.direction: Direction = direction
        self.domain: Domain = domain
        self.left_claw: int = 0
        self.right_claw: int = 0
        self.brain: int = 0
        self.last_fetch: int = 0
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

    def left_swap(self) -> int:
        self.brain, self.left_claw = self.left_claw, self.brain
        return self.brain

    def right_swap(self) -> int:
        self.brain, self.right_claw = self.right_claw, self.brain
        return self.brain

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

    def update(self) -> Generator[LobsterState, int, None]:
        # fetch-decode-execute

        # fetch
        fetch = yield LobsterState.FETCH

        # decode
        decoded = (fetch - self.last_fetch) & 255  # fit in 8 bits
        decoded = decoded if decoded < 128 else (256 - decoded)
        self.last_fetch = fetch
        is_instr = (decoded & 1)  # is last bit set?

        # execute
        if not is_instr:
            self.brain = self.last_fetch
        else:
            yield from self.execute(decoded)

        # increment program counter
        self.step()

    def execute(self, instr: int) -> Generator[LobsterState, int, None]:
        # oh boy this is gonna be a decently sized function

        # no-op
        if instr <= 7:
            pass

        # halt
        elif instr == 9:
            yield LobsterState.HALT

        # left swap
        elif instr == 11:
            self.left_swap()

        # right swap
        elif instr == 13:
            self.right_swap()

        # add
        elif instr == 15:
            self.add()

        # subtract
        elif instr == 17:
            self.sub()

        # multiply
        elif instr == 19:
            self.mul()

        # divide
        elif instr == 21:
            self.div()

        # read from pointer
        elif instr == 23:
            self.brain = yield LobsterState.READ

        # write to pointer
        elif instr == 25:
            yield LobsterState.WRITE

        # shift pointer by x, y (2 reads)
        elif instr == 27:
            self.step()
            x_offs = yield LobsterState.FETCH
            self.step()
            y_offs = yield LobsterState.FETCH
            self.shift_pointer(Point(x_offs, y_offs))

        # write to next position
        elif instr == 29:
            self.step()
            yield LobsterState.MODIFY

        # turn left (counter-clockwise)
        elif instr == 31:
            self.turn(-1)

        # turn right (clockwise)
        elif instr == 33:
            self.turn(1)

        # turn left if 0
        elif instr == 35:
            if not self.brain:
                self.turn(-1)

        # turn right if 0
        elif instr == 37:
            if not self.brain:
                self.turn(1)

        # turn left if not 0
        elif instr == 39:
            if self.brain:
                self.turn(-1)

        # turn right if not 0
        elif instr == 41:
            if self.brain:
                self.turn(1)

        # clone
        elif instr == 43:
            yield LobsterState.CLONE

        # print
        elif instr == 45:
            print("lobster say:", self.brain)

        # input
        elif instr == 47:
            self.brain = int(input("> "))
