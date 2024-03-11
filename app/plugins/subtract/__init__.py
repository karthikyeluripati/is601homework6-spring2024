import logging
from app.commands import Command


class SubtractCommand(Command):
    def execute(self):
        operand1 = float(input("Enter the first operand: "))
        operand2 = float(input("Enter the second operand: "))

        try:
            result = self.sub(operand1, operand2)
            self.log_success(result)
            return result
        except Exception as e:
            self.log_error(e)
            raise

    def sub(self, operand1, operand2):
        logging.info("Subtraction started")
        result = operand1 - operand2
        return result

    def log_success(self, result):
        logging.info(f"Subtraction completed. Result: {result}")
        print(f"The result of subtraction is: {result}")

    def log_error(self, error):
        logging.error(f"Error during subtraction: {error}")
        print(f"Error during subtraction: {error}")