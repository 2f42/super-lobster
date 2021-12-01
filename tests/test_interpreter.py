import superlobster.interpreter as sl
from unittest import TestCase


class TestPoint(TestCase):

    def test_creation(self):
        p = sl.Point()
        self.assertIsInstance(p, sl.Point)
        self.assertEqual(p.x, 0)
        self.assertEqual(p.y, 0)

        p = sl.Point(3, 4)
        self.assertIsInstance(p, sl.Point)
        self.assertEqual(p.x, 3)
        self.assertEqual(p.y, 4)

        p = sl.Point(-3, 4)
        self.assertIsInstance(p, sl.Point)
        self.assertEqual(p.x, -3)
        self.assertEqual(p.y, 4)

    def test_equality(self):
        p = sl.Point(2, 3)
        self.assertTrue(p == sl.Point(2, 3))
        self.assertFalse(p == sl.Point())
        self.assertFalse(p != sl.Point(2, 3))
        self.assertTrue(p != sl.Point())
        self.assertFalse(p == 0)

    def test_immutability(self):
        p = sl.Point(1, 2)
        with self.assertRaises(AttributeError):
            p.x = 3
        with self.assertRaises(AttributeError):
            p.y = 3
        self.assertEqual(p, sl.Point(1, 2))

    def test_addition(self):
        a = sl.Point(1, 2)
        b = sl.Point(3, 4)

        c = a + b
        self.assertIsInstance(c, sl.Point)
        self.assertEqual(c, sl.Point(4, 6))

        with self.assertRaises(TypeError):
            a + 3
        with self.assertRaises(TypeError):
            a + "a"

        b += sl.Point(1, 1)
        self.assertIsInstance(b, sl.Point)
        self.assertEqual(b, sl.Point(4, 5))

    def test_subtraction(self):
        a = sl.Point(1, 2)
        b = sl.Point(3, 4)

        c = b - a
        self.assertIsInstance(c, sl.Point)
        self.assertEqual(c, sl.Point(2, 2))

        with self.assertRaises(TypeError):
            a - 3
        with self.assertRaises(TypeError):
            a - "a"

        b -= sl.Point(1, 1)
        self.assertIsInstance(b, sl.Point)
        self.assertEqual(b, sl.Point(2, 3))

    def test_multiplication(self):
        a = sl.Point(1, 2)
        b = sl.Point(3, 4)

        c = a * 3
        self.assertIsInstance(c, sl.Point)
        self.assertEqual(c, sl.Point(3, 6))

        d = a * b
        self.assertIsInstance(d, sl.Point)
        self.assertEqual(d, sl.Point(3, 8))

        with self.assertRaises(TypeError):
            a * .3
        with self.assertRaises(TypeError):
            a * "a"

        b *= 4
        self.assertIsInstance(b, sl.Point)
        self.assertEqual(b, sl.Point(12, 16))


class TestDirection(TestCase):

    def test_direction(self):
        d = sl.Direction.EAST
        self.assertIsInstance(d, sl.Direction)
        self.assertIs(d, sl.Direction.EAST)

    def test_immutability(self):
        d = sl.Direction.EAST
        with self.assertRaises(AttributeError):
            d.value = 3
        self.assertIs(d, sl.Direction.EAST)

    def test_turning(self):
        d = sl.Direction.EAST
        d += 1
        self.assertIs(d, sl.Direction.SOUTH)
        d += 4
        self.assertIs(d, sl.Direction.SOUTH)
        d += 31
        self.assertIs(d, sl.Direction.EAST)
        d -= 1
        self.assertIs(d, sl.Direction.NORTH)

    def test_conversion_to_point(self):
        d = sl.Direction.EAST
        self.assertEqual(sl.Point.from_direction(d), sl.Point(1, 0))
        d += 1
        self.assertEqual(sl.Point.from_direction(d), sl.Point(0, 1))
        d += 1
        self.assertEqual(sl.Point.from_direction(d), sl.Point(-1, 0))
        d += 1
        self.assertEqual(sl.Point.from_direction(d), sl.Point(0, -1))
