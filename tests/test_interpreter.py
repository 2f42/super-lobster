import superlobster.interpreter as sl
from unittest import TestCase


class TestLobster(TestCase):

    def test_creation(self):
        barry = sl.Lobster(sl.Point(3, 4), sl.Direction.SOUTH)
        self.assertEqual(barry.position, sl.Point(3, 4))
        self.assertIs(barry.direction, sl.Direction.SOUTH)

        claire = sl.Lobster()
        self.assertIsNot(barry, claire)
        self.assertNotEqual(barry.id, claire.id)
        self.assertEqual(claire.position, sl.Point(0, 0))
        self.assertIs(claire.direction, sl.Direction.EAST)

        self.assertEqual(barry.position, sl.Point(3, 4))
        self.assertIs(barry.direction, sl.Direction.SOUTH)

    def test_stepping(self):
        barry = sl.Lobster()
        self.assertEqual(barry.position, sl.Point(0, 0))
        barry.step()
        self.assertEqual(barry.position, sl.Point(1, 0))
        barry.step(3)
        self.assertEqual(barry.position, sl.Point(4, 0))

    def test_turning(self):
        barry = sl.Lobster(direction=sl.Direction.SOUTH)
        self.assertIs(barry.direction, sl.Direction.SOUTH)
        barry.turn(3)
        self.assertIs(barry.direction, sl.Direction.EAST)
        barry.turn(5)
        self.assertIs(barry.direction, sl.Direction.SOUTH)

    def test_movement(self):
        barry = sl.Lobster(sl.Point(3, 4), sl.Direction.SOUTH)
        barry.turn(2)
        barry.step(4)
        self.assertEqual(barry.position, sl.Point(3, 0))
        barry.turn(-1)
        barry.step(3)
        self.assertEqual(barry.position, sl.Point(0, 0))
