import sys
from utils.logger import get_logger

logger = get_logger(__name__)


class CustomException(Exception):
    """
    Custom exception class for the Flipkart Recommender application.
    Provides detailed error messages with file name and line number information.
    """

    def __init__(self, error_message: str, error_detail: sys):
        """
        Initialize custom exception.

        Args:
            error_message: The error message
            error_detail: System error details (typically sys)
        """
        super().__init__(error_message)
        self.error_message = self._get_detailed_error_message(error_message, error_detail)
        logger.error(self.error_message)

    @staticmethod
    def _get_detailed_error_message(error_message: str, error_detail: sys) -> str:
        """
        Format error message with file and line information.

        Args:
            error_message: The error message
            error_detail: System error details

        Returns:
            Formatted error message string
        """
        _, _, exc_tb = error_detail.exc_info()

        if exc_tb is not None:
            file_name = exc_tb.tb_frame.f_code.co_filename
            line_number = exc_tb.tb_lineno
            return f"Error occurred in script: [{file_name}] at line [{line_number}]: {error_message}"

        return f"Error: {error_message}"

    def __str__(self):
        return self.error_message


class DataIngestionException(CustomException):
    """Exception raised during data ingestion process."""
    pass


class ModelException(CustomException):
    """Exception raised during model operations."""
    pass


class ConfigurationException(CustomException):
    """Exception raised for configuration errors."""
    pass
