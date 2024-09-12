from main import logging
from main import datetime

class TypeChecker:
    """Error handler class containing a bunch of checks."""
    def __init__(self, log_file="error.log"):
        logging = logging(__name__)
    
    def log_error(self, error_message):
        """Logs error to a file"""
        logging.error(error_message)
    
    def check_int(self, value):
        """Checks if result is a integer."""
        if isinstance(value, int):
            return value
        elif isinstance(value, float):
            self.log_error(f"Float {value} was entered. Converting to int: {int(value)}.")
            return int(value)
        elif isinstance(value, str):
            if value.isdigit():
                return int(value)
            try:
                return int(round(float(value)))
            except ValueError:
                self.log_error(f"ValueError: string '{value}' cannot be converted to int.")
                return None
        else:
            self.log_error(f"TypeError: {type(value)} could not be converted to int")
            return None
            
    
    def check_float(self, value):
        """Checks if result is a float."""
        if isinstance(value, float):
            return value
        elif isinstance(value, int):
            self.log_error(f"Integer {value} was entered. Converting to float: {float(value)}.")
            return float(value)
        elif isinstance(value, str):
            try:
                return float(value)
            except ValueError:
                self.log_error(f"ValueError: str '{value}' cannot be converted to float.")
                return None
        elif isinstance(value, (datetime.date, datetime.datetime)):
            self.log_error(f"Date '{value}' could not be converted into float")
            return None
        else:
            self.log_error(f"TypeError: {type(value)} is not a float")
            return None
    
    def check_date(self, value):
        """Checks if result is date/datetime"""
        if isinstance(value, datetime):
            return value
        elif isinstance(value, (int, float)):
                self.log_error(f"{value} cannot be converted to datetime.")
                return None
        elif isinstance(value, str):
            try:
                self.log_error(f"Converting str '{value}' to datetime object")
                return datetime.strptime(value, "%Y-%m-%d")
            except ValueError:
                self.log_error(f"ValueError: str '{value}' cannot be converted to date")
        else:
            self.log_error(f"TypeError: {type(value)} is not a valid date")
            return None

type_checker = TypeChecker()
logging.info("TypeChecker executed..")