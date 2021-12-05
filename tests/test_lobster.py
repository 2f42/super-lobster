import superlobster.lobster as sl
from superlobster.geometry import ClosedDomain
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

        derek = sl.Lobster(sl.Point(10, 10), domain=ClosedDomain(5, 5))
        self.assertIsNot(derek, barry)
        self.assertNotEqual(derek, barry)
        self.assertEqual(derek.position, sl.Point(0, 0))

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

    def test_movement_closed_domain(self):
        barry = sl.Lobster(sl.Point(3, 4), sl.Direction.SOUTH, ClosedDomain(5, 7))
        self.assertEqual(barry.position, sl.Point(3, 4))
        barry.step(2)
        self.assertEqual(barry.position, sl.Point(3, 6))
        barry.step(2)
        self.assertEqual(barry.position, sl.Point(3, 1))

    def test_cloning(self):
        barry = sl.Lobster(sl.Point(3, 4), sl.Direction.SOUTH, ClosedDomain(5, 7))

        barry2 = barry.clone()
        self.assertIsNot(barry, barry2)
        self.assertEqual(barry2.position, sl.Point(2, 4))
        self.assertIs(barry2.direction, sl.Direction.SOUTH)
        self.assertIs(barry.domain, barry2.domain)

        barry3 = barry.clone(barry.direction - 1, sl.Direction.NORTH)
        self.assertIsNot(barry, barry3)
        self.assertEqual(barry3.position, sl.Point(4, 4))
        self.assertIs(barry3.direction, sl.Direction.NORTH)
        self.assertIs(barry.domain, barry3.domain)
