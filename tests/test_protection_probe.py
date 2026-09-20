"""Intentional required-check failure probe. Not a product test."""

import unittest


class TestProtectionProbe(unittest.TestCase):
    def test_intentional_required_check_failure(self):
        self.fail(
            "intentional required-check failure for branch protection probe"
        )
