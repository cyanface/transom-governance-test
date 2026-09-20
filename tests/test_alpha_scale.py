"""Alpha scale suite: scaled multiplier behavior."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import alpha


class TestAlphaScale(unittest.TestCase):
    def test_scaled_zero(self):
        self.assertEqual(alpha.scaled(0), 0)

    def test_scaled_negative_one(self):
        self.assertEqual(alpha.scaled(-1), -1)

    def test_scaled_two(self):
        self.assertEqual(alpha.scaled(2), 2)


if __name__ == "__main__":
    unittest.main()
