import unittest

from glasses import TriangularGlassStack


class TestTriangularGlassStack(unittest.TestCase):
    def test_add_liquid_basic(self):
        """
        Test basic version of add_liquid with no overflow
        """
        stack = TriangularGlassStack()
        stack.add_liquid(0)
        self.assertEqual(stack.rows, [])

        stack = TriangularGlassStack()
        stack.add_liquid(1)
        self.assertEqual(stack.rows, [[1]])

        stack = TriangularGlassStack()
        stack.add_liquid(250)
        self.assertEqual(stack.rows, [[250]])

    def test_add_liquid_with_overflow(self):
        """
        Test add_liquid with overflow
        """
        stack = TriangularGlassStack()
        stack.add_liquid(251)
        self.assertEqual(stack.rows, [[250], [1/2, 1/2]])

        stack = TriangularGlassStack()
        stack.add_liquid(250 * 3)
        self.assertEqual(stack.rows, [[250], [250, 250]])

        stack = TriangularGlassStack()
        stack.add_liquid(250 * 3 + 1)
        self.assertEqual(stack.rows, [[250], [250, 250], [1/3, 1/3, 1/3]])

        stack = TriangularGlassStack()
        stack.add_liquid(250 * 9)
        self.assertEqual(stack.rows, [[250], [250, 250], [250, 250, 250],
                                      [750/4, 750/4, 750/4, 750/4]])

    def test_add_liquid_negative(self):
        """
        Test add_liquid when you try to add a negaive amount of liquid
        """
        stack = TriangularGlassStack()

        with self.assertRaises(ValueError):
            stack.add_liquid(-1)


if __name__ == '__main__':
    unittest.main()
