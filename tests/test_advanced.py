# -*- coding: utf-8 -*-

from .context import __PROJECT-NAME__

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        self.assertIsNone(__PROJECT-NAME__.hmm())


if __name__ == '__main__':
    unittest.main()
