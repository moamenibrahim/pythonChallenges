import unittest
import typing
from io import StringIO
from ddt import data, ddt, unpack
from src.introduction import Introduction


@ddt
class TestIntroduction(unittest.TestCase):

    def setUp(self):
        self.out = StringIO()
        self.introduction = Introduction(self.out)

    def tearDown(self):
        self.out = None

    @staticmethod
    def capture_stdout(self):
        pass

    def test_hello_world(self):
        self.assertEqual(self.introduction.hello_world(), "hello world")

    @data((10, "Weird"),
          (4, "Not Weird"),
          (10.9, "Weird"),
          (22, "Not Weird"),
          (-10000, ""))
    @unpack
    def test_conditions(self, number: int, expected: str):
        self.introduction.conditions(number)
        self.assertEqual(expected, self.out.getvalue())

    @data((1, 2, "3 -1 2 "),
          (2, -4, "-2 6 -8 "),
          (10.9, 11.88, "22.78 -0.9800000000000004 129.49200000000002 "),
          (-5, -10000, "-10005 9995 50000 "))
    @unpack
    def test_arithmetic_operators(self, first_integer: int, second_integer: int, expected: str):
        self.introduction.arithmetic_operators(first_integer, second_integer)
        self.assertEqual(expected, self.out.getvalue())

    @data((1, 2, "0.5 0.5 "),
          (2, -4, "-0.5 -0.5 "),
          (10.9, 11.88, "0.9175084175084175 0.9175084175084175 "),
          (-10, -5, "2.0 2.0 "))
    @unpack
    def test_division_operation(self, first_integer: int, second_integer: int, expected: str):
        self.introduction.division_operation(first_integer, second_integer)
        self.assertEqual(expected, self.out.getvalue())

    @data((1, "0"),
          (5, "0 1 4 9 16"))
    @unpack
    def test_loops(self, input: int, expected: str):
        self.introduction.loops(input)
        self.assertEqual(expected, self.out.getvalue())

    @data((2000, "True"),
          (1800, "False"),
          (2100, "False"),
          (1992, "True"))
    @unpack
    def test_loops(self, input: int, expected: str):
        self.introduction.is_leap(input)
        self.assertEqual(expected, self.out.getvalue())

    @data((3, "123"),
          (0, ""),
          (5, "12345"))
    @unpack
    def test_loops(self, input: int, expected: str):
        self.introduction.print_future(input)
        self.assertEqual(expected, self.out.getvalue())
