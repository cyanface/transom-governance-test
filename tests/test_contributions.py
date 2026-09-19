"""Baseline suite: per-module contributions and combined total."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import alpha
import beta
import gamma


class TestAlpha(unittest.TestCase):
    def test_contribution(self):
        self.assertEqual(alpha.contribution(), 1)


class TestBeta(unittest.TestCase):
    def test_contribution(self):
        self.assertEqual(beta.contribution(), 2)


class TestGamma(unittest.TestCase):
    def test_contribution(self):
        self.assertEqual(gamma.contribution(), 3)


class TestCombination(unittest.TestCase):
    def test_total(self):
        total = alpha.contribution() + beta.contribution() + gamma.contribution()
        self.assertEqual(total, 6)
