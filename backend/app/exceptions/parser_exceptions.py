# backend/app/exceptions/parser_exceptions.py

class ParserException(Exception):
    """Raised when document parsing fails."""
    # """Unable to parse PDF document."""
    default_message = "Failed to parse document."
       
    def __init__(self, message: str | None = None):
        super().__init__(message or self.default_message)

class ParserServiceException(ParserException):
    """Raised when the parser service encounters an error."""
    default_message = "Parser service failed."

