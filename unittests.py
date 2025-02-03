import unittest
from list_based_analysis import check_signal_state_transition


class TestCheckSignalStates(unittest.TestCase):
    def test_basic_valid_sequence(self):
        """Test a simple valid sequence"""
        signal = [1, 1, 1, 2, 2, 3]
        expected = [1, 2, 3]
        self.assertTrue(check_signal_state_transition(signal, expected))

    def test_repeated_sequence(self):
        """Test a sequence that appears twice (should fail)"""
        signal = [1, 2, 3, 1, 2, 3]
        expected = [1, 2, 3]
        self.assertFalse(check_signal_state_transition(signal, expected))

    def test_empty_inputs(self):
        """Test empty inputs"""
        self.assertFalse(check_signal_state_transition([], [1, 2, 3]))
        self.assertFalse(check_signal_state_transition([1, 2, 3], []))
        self.assertFalse(check_signal_state_transition([], []))

    def test_partial_sequence(self):
        """Test incomplete sequence"""
        signal = [1, 1, 2]
        expected = [1, 2, 3]
        self.assertFalse(check_signal_state_transition(signal, expected))

    def test_non_numeric(self):
        """Test when sequence contain non-numeric entry"""
        signal = [1, 2, "A"]
        expected = [1, 2, "A"]
        self.assertTrue(check_signal_state_transition(signal, expected))

    def test_no_sequence(self):
        """Test when sequence is not present"""
        signal = [4, 5, 6]
        expected = [1, 2, 3]
        self.assertFalse(check_signal_state_transition(signal, expected))


if __name__ == '__main__':
    unittest.main()
