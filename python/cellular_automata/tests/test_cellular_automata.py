import unittest
from cellular_automata.ca import transition, sliding_window
from cellular_automata.rules import to_bin, rule


class TestCA(unittest.TestCase):
    def test_transition_expected(self):
        state = [0, 0, 1, 0, 0]
        expected = [0, 1, 1, 1, 0]
        self.assertEqual(transition(state), expected)


class TestRules(unittest.TestCase):
    def test_rule(self):
        pass

if __name__ == "__main__":
    unittest.main()
