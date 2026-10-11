"""The plug-in exposes the memory under the method's name Rb-ERI as well as its earlier name (decision D-224-NAME)."""

from __future__ import annotations

import unittest

import vsmt_memory
from vsmt_memory import RbERIMemory, VSMTMemory
from vsmt_memory.memory import ARM


class NameAliasTests(unittest.TestCase):
    def test_rb_eri_memory_is_the_same_class(self) -> None:
        self.assertIs(RbERIMemory, VSMTMemory)
        self.assertIn("RbERIMemory", vsmt_memory.__all__)
        self.assertIn("VSMTMemory", vsmt_memory.__all__)

    def test_the_arm_key_of_the_frozen_runs_is_unchanged(self) -> None:
        self.assertEqual(ARM, "VSMT-lean")


if __name__ == "__main__":
    unittest.main()
