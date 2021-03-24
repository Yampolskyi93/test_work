import unittest
import pytest

from test_work import test_work


class TestGetTwoMax(unittest.TestCase):
    def test_full_filled_list(self):
        self.assertSequenceEqual(test_work.get_2_max([32, 11, 0, -107, 4, 15]), (32, 15))

    def test_list_with_one_element(self):
        self.assertSequenceEqual(test_work.get_2_max([32]), (32, None))

    def test_empty_list(self):
        self.assertSequenceEqual(test_work.get_2_max([]), (None, None))

    def test_list_with_equal_elements(self):
        self.assertSequenceEqual(test_work.get_2_max([1, 1, 1, 1, 1, 1]), (1, 1))
