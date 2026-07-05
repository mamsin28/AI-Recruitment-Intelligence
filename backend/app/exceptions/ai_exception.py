# backend/app/exceptions/ai_exception.py

class AI_Exception(Exception):
    """
    Base exception for all AI-related errors.
    """  
    default_message = "AI processing error."

    def __init__(self, message: str | None = None):
        super().__init__(message or self.default_message)

class EmbeddingException(Exception):
    """
    Base exception for all embedding-related errors.
    """
    default_message = "Embedding processing error."

class RetrieverException(Exception):
    """
    Base exception for all retriever-related errors.
    """
    default_message = "Retriever processing error."

class LLMException(Exception):
    """
    Base exception for all LLM-related errors.
    """
    default_message = "LLM processing error."
