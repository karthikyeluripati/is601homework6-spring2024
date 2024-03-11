import unittest
from unittest.mock import patch
from app.plugins.add import AddCommand

class TestaddtractCommand(unittest.TestCase):
    @patch("builtins.input", side_effect=["5", "2"])
    def test_execute_addtracts_operands(self, mock_input):
        add_command = AddCommand()
        result = add_command.execute()
        self.assertEqual(result, 7)

if __name__ == "__main__":
    unittest.main()
