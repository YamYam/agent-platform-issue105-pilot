import unittest
import grid

class BaselineTests(unittest.TestCase):
    def test_fixture_starts_without_an_implementation(self):
        with self.assertRaises(NotImplementedError):
            grid.normalize_grid({})
