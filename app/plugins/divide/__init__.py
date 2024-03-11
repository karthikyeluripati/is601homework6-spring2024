import logging
from app.commands import Command


class DivisionCommand(Command):
    def execute(self):
        operand1 = float(input("Enter the first operand: "))
        operand2 = float(input("Enter the second operand: "))

        try:
            result = self.div(operand1, operand2)
            self.log_success(result)
            return result
        except ZeroDivisionError as zde:
            self.log_error(f"Error during division: {zde}")
        except Exception as e:
            self.log_error(e)
            raise

    def div(self, operand1, operand2):
        logging.info("Division started")
        if operand2 == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        result = operand1 / operand2
        return result

    def log_success(self, result):
        logging.info(f"Division completed. Result: {result}")
        print(f"The result of Division is: {result}")

    def log_error(self, error):
        logging.error(f"Error during Division: {error}")
        print(f"Error during Division: {error}")
