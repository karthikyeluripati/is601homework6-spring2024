import unittest
from unittest.mock import patch
from app.plugins.multiply import MultiplyCommand

class TestMultiplyCommand(unittest.TestCase):
    @patch("builtins.input", side_effect=["5", "2"])
    def test_execute_multiplies_operands(self, mock_input):
        multiply_command = MultiplyCommand()
        result = multiply_command.execute()
        self.assertEqual(result, 10)

    @patch("builtins.input", side_effect=["abc", "2"])  # Invalid input for operand1
    def test_execute_handles_invalid_input_operand1(self, mock_input):
        multiply_command = MultiplyCommand()
        with self.assertRaises(ValueError):
            multiply_command.execute()

    @patch("builtins.input", side_effect=["5", "xyz"])  # Invalid input for operand2
    def test_execute_handles_invalid_input_operand2(self, mock_input):
        multiply_command = MultiplyCommand()
        with self.assertRaises(ValueError):
            multiply_command.execute()

    def test_multiplies_operands(self):
        multiply_command = MultiplyCommand()
        result = multiply_command.multiply(5, 2)
        self.assertEqual(result, 10)

    @patch("builtins.input", side_effect=["abc", "2"])  # Invalid input for operand1
    def test_multiply_handles_invalid_input_operand1(self, mock_input):
        multiply_command = MultiplyCommand()
        with self.assertRaises(ValueError):
            multiply_command.execute()  # Check for ValueError during execute

    @patch("builtins.input", side_effect=["5", "xyz"])  # Invalid input for operand2
    def test_multiply_handles_invalid_input_operand2(self, mock_input):
        multiply_command = MultiplyCommand()
        with self.assertRaises(ValueError):
            multiply_command.execute()  # Check for ValueError during execute

if __name__ == "__main__":
    unittest.main()
