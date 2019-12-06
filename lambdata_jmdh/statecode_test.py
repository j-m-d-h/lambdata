import unittest
from statecode import State

class StateCodeTest(unittest.TestCase):
    """Tests the full_state method in statecode"""
    def test_full_state(self):
        self.assertEqual(State('TX').full_state(), 'Texas')

if __name__ == '__main__':
    unittest.main()
