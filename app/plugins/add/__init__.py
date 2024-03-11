import logging
from app.commands import Command


class AddCommand(Command):
    def execute(self):
        operand1 = float(input("Enter the first operand: "))
        operand2 = float(input("Enter the second operand: "))

        try:
            result = self.add(operand1, operand2)
            self.log_success(result)
            return result
        except Exception as e:
            self.log_error(e)
            raise

    def add(self, operand1, operand2):
        logging.info("Addition started")
        result = operand1 + operand2
        return result

    def log_success(self, result):
        logging.info(f"Addition completed. Result: {result}")
        print(f"The result of addition is: {result}")

    def log_error(self, error):
        logging.error(f"Error during addition: {error}")
        print(f"Error during addition: {error}")