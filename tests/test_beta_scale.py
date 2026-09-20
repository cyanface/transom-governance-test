"""Scale tests for beta module."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import beta


class TestBetaScale(unittest.TestCase):
    def test_scaled_zero(self):
        self.assertEqual(beta.scaled(0), 0)

    def test_scaled_negative_one(self):
        self.assertEqual(beta.scaled(-1), -2)

    def test_scaled_two(self):
        self.assertEqual(beta.scaled(2), 4)
