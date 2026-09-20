"""Scale tests for gamma module."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import gamma


class TestGammaScale(unittest.TestCase):
    def test_scaled_zero(self):
        self.assertEqual(gamma.scaled(0), 0)

    def test_scaled_negative_one(self):
        self.assertEqual(gamma.scaled(-1), -3)

    def test_scaled_two(self):
        self.assertEqual(gamma.scaled(2), 6)


if __name__ == "__main__":
    unittest.main()
