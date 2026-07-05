# backend/app/config/constants.py

"""
Application-wide constants.
"""

SUPPORTED_DOCUMENT_TYPES = {
    ".pdf",
    ".docx",
}

MAX_DOCUMENT_SIZE_MB = 20
# MAX_UPLOAD_SIZE = 20 * 1024 * 1024
MAX_DOCUMENT_SIZE_BYTES = MAX_DOCUMENT_SIZE_MB * 1024 * 1024

DEFAULT_CHUNK_SIZE = 500

DEFAULT_CHUNK_OVERLAP = 100

