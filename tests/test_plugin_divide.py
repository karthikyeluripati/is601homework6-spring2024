import unittest
from unittest.mock import patch
from app.plugins.divide import DivisionCommand

class TestDivisionCommand(unittest.TestCase):
    @patch("builtins.input", side_effect=["6", "2"])
    def test_execute_divides_operands(self, mock_input):
        division_command = DivisionCommand()
        result = division_command.execute()
        self.assertEqual(result, 3.0)

    @patch("builtins.input", side_effect=["abc", "2"])  # Invalid input for operand1
    def test_execute_handles_invalid_input_operand1(self, mock_input):
        division_command = DivisionCommand()
        with self.assertRaises(ValueError):
            division_command.execute()

    @patch("builtins.input", side_effect=["6", "xyz"])  # Invalid input for operand2
    def test_execute_handles_invalid_input_operand2(self, mock_input):
        division_command = DivisionCommand()
        with self.assertRaises(ValueError):
            division_command.execute()

    def test_divides_operands(self):
        division_command = DivisionCommand()
        result = division_command.div(6, 2)
        self.assertEqual(result, 3.0)

    @patch("builtins.input", side_effect=["abc", "2"])  # Invalid input for operand1
    def test_div_handles_invalid_input_operand1(self, mock_input):
        division_command = DivisionCommand()
        with self.assertRaises(ValueError) as context:
            division_command.div(float("abc"), 2)

        self.assertIn("could not convert string to float:", str(context.exception))

    @patch("builtins.input", side_effect=["6", "xyz"])  # Invalid input for operand2
    def test_div_handles_invalid_input_operand2(self, mock_input):
        division_command = DivisionCommand()
        with self.assertRaises(ValueError) as context:
            division_command.div(6, float("xyz"))

        self.assertIn("could not convert string to float:", str(context.exception))

if __name__ == "__main__":
    unittest.main()
