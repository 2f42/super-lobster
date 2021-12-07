from __future__ import annotations
from typing import Dict

from .geometry import Point, ClosedDomain
from .structs import Matrix
from .lobster import Lobster, LobsterState


class VirtualMachine:

    def __init__(self, matrix: Matrix) -> None:
        self.matrix: Matrix = matrix
        self.domain: ClosedDomain = ClosedDomain(matrix.width, matrix.height)
        self.lobsters: Dict[int, Lobster] = {}
        self.lobsters[0] = Lobster(domain=self.domain, pointer=Point(-1, -1))

    def update(self) -> None:
        scheduled_for_annihilation = []
        scheduled_for_addition = []

        for lob_id, lobster in self.lobsters.items():
            lob_gen = lobster.update()

            try:
                state: LobsterState = next(lob_gen)
                while True:
                    x, y = lobster.position.coords()
                    _x, _y = lobster.pointer.coords()
                    print(state.name)

                    if state is LobsterState.HALT:
                        scheduled_for_annihilation.append(lob_id)
                        state = next(lob_gen)

                    elif state is LobsterState.DONE:
                        state = next(lob_gen)

                    elif state is LobsterState.FETCH:
                        state = lob_gen.send(self.matrix.get(x, y))

                    elif state is LobsterState.READ:
                        state = lob_gen.send(self.matrix.get(_x, _y))

                    elif state is LobsterState.MODIFY:
                        self.matrix.set(x, y, lobster.brain)
                        state = next(lob_gen)

                    elif state is LobsterState.WRITE:
                        self.matrix.set(_x, _y, lobster.brain)
                        state = next(lob_gen)

                    elif state is LobsterState.CLONE:
                        scheduled_for_addition.append(lobster.clone())
                        state = next(lob_gen)

            except StopIteration:
                pass

        for lobster in scheduled_for_addition:
            self.lobsters[lobster.id] = lobster

        for lob_id in scheduled_for_annihilation:
            del self.lobsters[lob_id]

    def run(self, max_steps: int = 0) -> None:
        if max_steps == 0:
            while self.lobsters:
                self.update()
        else:
            for i in range(max_steps):
                self.update()
