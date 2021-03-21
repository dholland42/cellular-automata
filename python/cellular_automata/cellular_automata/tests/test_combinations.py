import unittest

from combinations import CombinationsCA

class TestCombinationsCA(unittest.TestCase):
    def test_initial_state_default(self):
        ca = CombinationsCA()
        self.assertEqual(ca.value, [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0])


if __name__ == "__main__":
    unittest.main()
