import unittest

from glasses import TriangularGlassStack

class TestTriangularGlassStack(unittest.TestCase):
    def setUp(self):
        pass

    def test_add_liquid_basic(self):
        stack = TriangularGlassStack()
        stack.add_liquid(0)
        self.assertEqual(stack.row, [[0]])

        stack = TriangularGlassStack()
        stack.add_liquid(1)
        self.assertEqual(stack.row, [[1]])

        stack = TriangularGlassStack()
        stack.add_liquid(250)
        self.assertEqual(stack.row, [[250]])


if __name__ == '__main__':
    unittest.main()
