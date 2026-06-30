from io import BytesIO
from pathlib import Path

import fitz
from docx import Document

from app.config.logging_config import get_logger

logger = get_logger(__name__)


class ParserException(Exception):
    """Raised when document parsing fails."""


class PDFParser:
    """Parser for PDF documents."""

    def extract_text(self, content: bytes) -> str:
        text = []

        try:
            with fitz.open(stream=content, filetype="pdf") as pdf:
                logger.info("PDF opened successfully.")

                for page in pdf:
                    text.append(page.get_text())

                logger.info(
                    "PDF parsed successfully (%s pages).",
                    len(pdf),
                )

            return "\n".join(text).strip()

        except Exception as exc:
            logger.exception("Failed to parse PDF document.")
            raise ParserException("Unable to parse PDF document.") from exc


class DOCXParser:
    """Parser for Microsoft Word documents."""

    def extract_text(self, content: bytes) -> str:
        try:
            document = Document(BytesIO(content))

            text = "\n".join(
                paragraph.text
                for paragraph in document.paragraphs
            ).strip()

            logger.info("DOCX parsed successfully.")

            return text

        except Exception as exc:
            logger.exception("Failed to parse DOCX document.")
            raise ParserException("Unable to parse DOCX document.") from exc


class ParserService:
    """
    Service responsible for selecting the correct parser
    based on the uploaded document type.
    """

    def __init__(self) -> None:
        self._parsers = {
            ".pdf": PDFParser(),
            ".docx": DOCXParser(),
        }

    def extract_text(
        self,
        filename: str,
        content: bytes,
    ) -> str:
        extension = Path(filename).suffix.lower()

        logger.info("Selecting parser for '%s'.", extension)

        parser = self._parsers.get(extension)

        if parser is None:
            logger.error("Unsupported file type: %s", extension)
            raise ParserException(
                f"Unsupported file type: {extension}"
            )

        logger.info("Parsing started for '%s'.", filename)

        text = parser.extract_text(content)

        logger.info(
            "Parsing completed successfully. Extracted %s characters.",
            len(text),
        )

        return text