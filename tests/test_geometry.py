import superlobster.geometry as g
from unittest import TestCase


class TestPoint(TestCase):

    def test_creation(self):
        p = g.Point()
        self.assertIsInstance(p, g.Point)
        self.assertEqual(p.x, 0)
        self.assertEqual(p.y, 0)

        p = g.Point(3, 4)
        self.assertIsInstance(p, g.Point)
        self.assertEqual(p.x, 3)
        self.assertEqual(p.y, 4)

        p = g.Point(-3, 4)
        self.assertIsInstance(p, g.Point)
        self.assertEqual(p.x, -3)
        self.assertEqual(p.y, 4)

    def test_equality(self):
        p = g.Point(2, 3)
        self.assertTrue(p == g.Point(2, 3))
        self.assertFalse(p == g.Point())
        self.assertFalse(p != g.Point(2, 3))
        self.assertTrue(p != g.Point())
        self.assertFalse(p == 0)

    def test_immutability(self):
        p = g.Point(1, 2)
        with self.assertRaises(AttributeError):
            p.x = 3
        with self.assertRaises(AttributeError):
            p.y = 3
        self.assertEqual(p, g.Point(1, 2))

    def test_addition(self):
        a = g.Point(1, 2)
        b = g.Point(3, 4)

        c = a + b
        self.assertIsInstance(c, g.Point)
        self.assertEqual(c, g.Point(4, 6))

        with self.assertRaises(TypeError):
            a + 3
        with self.assertRaises(TypeError):
            a + "a"

        b += g.Point(1, 1)
        self.assertIsInstance(b, g.Point)
        self.assertEqual(b, g.Point(4, 5))

    def test_subtraction(self):
        a = g.Point(1, 2)
        b = g.Point(3, 4)

        c = b - a
        self.assertIsInstance(c, g.Point)
        self.assertEqual(c, g.Point(2, 2))

        with self.assertRaises(TypeError):
            a - 3
        with self.assertRaises(TypeError):
            a - "a"

        b -= g.Point(1, 1)
        self.assertIsInstance(b, g.Point)
        self.assertEqual(b, g.Point(2, 3))

    def test_multiplication(self):
        a = g.Point(1, 2)
        b = g.Point(3, 4)

        c = a * 3
        self.assertIsInstance(c, g.Point)
        self.assertEqual(c, g.Point(3, 6))

        d = a * b
        self.assertIsInstance(d, g.Point)
        self.assertEqual(d, g.Point(3, 8))

        with self.assertRaises(TypeError):
            a * .3
        with self.assertRaises(TypeError):
            a * "a"

        b *= 4
        self.assertIsInstance(b, g.Point)
        self.assertEqual(b, g.Point(12, 16))


class TestDirection(TestCase):

    def test_direction(self):
        d = g.Direction.EAST
        self.assertIsInstance(d, g.Direction)
        self.assertIs(d, g.Direction.EAST)

    def test_immutability(self):
        d = g.Direction.EAST
        with self.assertRaises(AttributeError):
            d.value = 3
        self.assertIs(d, g.Direction.EAST)

    def test_turning(self):
        d = g.Direction.EAST
        d += 1
        self.assertIs(d, g.Direction.SOUTH)
        d += 4
        self.assertIs(d, g.Direction.SOUTH)
        d += 31
        self.assertIs(d, g.Direction.EAST)
        d -= 1
        self.assertIs(d, g.Direction.NORTH)
        d -= 31
        self.assertIs(d, g.Direction.EAST)

    def test_conversion_to_point(self):
        d = g.Direction.EAST
        self.assertEqual(g.Point.from_direction(d), g.Point(1, 0))
        d += 1
        self.assertEqual(g.Point.from_direction(d), g.Point(0, 1))
        d += 1
        self.assertEqual(g.Point.from_direction(d), g.Point(-1, 0))
        d += 1
        self.assertEqual(g.Point.from_direction(d), g.Point(0, -1))
