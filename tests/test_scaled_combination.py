"""Scaled combination suite: alpha, beta, gamma scaled total."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import alpha
import beta
import gamma


class TestScaledCombination(unittest.TestCase):
    def test_scaled_values(self):
        self.assertEqual(
            (alpha.scaled(2), beta.scaled(3), gamma.scaled(4)),
            (2, 6, 12),
        )

    def test_scaled_sum(self):
        total = alpha.scaled(2) + beta.scaled(3) + gamma.scaled(4)
        self.assertEqual(total, 20)

    def test_scaled_boundary_values(self):
        self.assertEqual(
            (alpha.scaled(-2), beta.scaled(0), gamma.scaled(3)),
            (-2, 0, 9),
        )

    def test_scaled_boundary_sum(self):
        total = alpha.scaled(-2) + beta.scaled(0) + gamma.scaled(3)
        self.assertEqual(total, 7)

    def test_scaled_all_zero_values(self):
        self.assertEqual(
            (alpha.scaled(0), beta.scaled(0), gamma.scaled(0)),
            (0, 0, 0),
        )

    def test_scaled_all_zero_sum(self):
        total = alpha.scaled(0) + beta.scaled(0) + gamma.scaled(0)
        self.assertEqual(total, 0)


if __name__ == "__main__":
    unittest.main()
