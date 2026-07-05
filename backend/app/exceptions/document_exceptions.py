# app/exceptions/document_exceptions.py

class DocumentException(Exception):
    """
    Base exception for all document-related errors.
    """
    
    default_message = "Document processing error."

    def __init__(self, message: str | None = None):
        super().__init__(message or self.default_message)

class DocumentValidationException(DocumentException):
    """
    Raised when document validation fails.
    """
    default_message = "Uploaded document is not valid."

class EmptyDocumentException(DocumentException):
    """
    Raised when uploaded document is empty.
    """
    default_message = "Uploaded document is empty."

class UnsupportedDocumentException(DocumentException):
    """
    Raised when uploaded document type is unsupported.
    """
    default_message = "Uploaded document type is not supported."

class DocumentTooLargeException(DocumentException):
    """
    Raised when uploaded document exceeds allowed size.
    """
    default_message = "Uploaded document exceeds allowed size."

class CorruptedDocumentException(DocumentException):
    """
    Raised when document cannot be opened.
    """
    default_message = "Uploaded document is corrupted."