import unittest
from unittest.mock import patch
from app.plugins.subtract import SubtractCommand

class TestSubtractCommand(unittest.TestCase):
    @patch("builtins.input", side_effect=["5", "2"])
    def test_execute_subtracts_operands(self, mock_input):
        subtract_command = SubtractCommand()
        result = subtract_command.execute()
        self.assertEqual(result, 3)

    @patch("builtins.input", side_effect=["5", "2"])  # Valid inputs
    def test_execute_handles_valid_input(self, mock_input):
        subtract_command = SubtractCommand()
        result = subtract_command.execute()
        self.assertEqual(result, 3)

    @patch("builtins.input", side_effect=["abc", "2"])  # Invalid input for operand1
    def test_execute_handles_invalid_input_operand1(self, mock_input):
        subtract_command = SubtractCommand()
        with self.assertRaises(ValueError):
            subtract_command.execute()

    @patch("builtins.input", side_effect=["5", "xyz"])  # Invalid input for operand2
    def test_execute_handles_invalid_input_operand2(self, mock_input):
        subtract_command = SubtractCommand()
        with self.assertRaises(ValueError):
            subtract_command.execute()

    def test_subtracts_operands(self):
        subtract_command = SubtractCommand()
        result = subtract_command.sub(5, 2)
        self.assertEqual(result, 3)

    def test_sub_handles_invalid_input_operand1(self):
        subtract_command = SubtractCommand()
        with self.assertRaises(TypeError) as context:
            subtract_command.sub("abc", 2)

        self.assertIn("unsupported operand type(s) for -: 'str' and 'int'", str(context.exception))

    def test_sub_handles_invalid_input_operand2(self):
        subtract_command = SubtractCommand()
        with self.assertRaises(TypeError) as context:
            subtract_command.sub(5, "xyz")

        self.assertIn("unsupported operand type(s) for -: 'int' and 'str'", str(context.exception))

if __name__ == "__main__":
    unittest.main()
