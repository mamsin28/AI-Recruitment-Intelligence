# backend/app/services/document_service.py

from fastapi import UploadFile
from pathlib import Path

from app.config.logging_config import get_logger
from app.models.parsed_document import ParsedDocument

from app.exceptions.parser_exceptions import ParserException
from app.services.parser_service import ParserService

from app.exceptions.document_exceptions import (
    DocumentException,
    DocumentValidationException,
    EmptyDocumentException,
    UnsupportedDocumentException,
)

from app.config.constants import SUPPORTED_DOCUMENT_TYPES

logger = get_logger(__name__)

# we moved it to Exceptions module to keep the service clean and focused on its responsibilities
# class DocumentServiceException(Exception):
#     """Raised when document processing fails."""


class DocumentService:
    """
    Handles the complete document processing pipeline.

    Responsibilities:
    - Read uploaded file
    - Validate uploaded file
    - Delegate parsing to ParserService
    - Return ParsedDocument
    """

    # ALLOWED_EXTENSIONS = SUPPORTED_DOCUMENT_TYPES

    def __init__(
        self,
        parser_service: ParserService | None = None,
    ) -> None:
        self.parser_service = parser_service or ParserService()

    async def process_document(
        self,
        file: UploadFile,
    ) -> ParsedDocument:
        """
        Process an uploaded document.
        """

        logger.info(
            "Processing document '%s'.",
            file.filename,
        )

        self._validate(file)

        content = await self._read_file(file)

        try:
            document = self.parser_service.parse(
                filename=file.filename,
                content=content,
            )

            logger.info(
                "Document '%s' processed successfully.",
                file.filename,
            )

            return document

        # except ParserException as exc:
        #     logger.exception(
        #         "ParserService failed."
        #     )

        #     raise DocumentException(
        #         str(exc)
        #     ) from exc

        except ParserException:
            logger.exception("ParserService failed.")
            raise

    async def _read_file(
        self,
        file: UploadFile,
    ) -> bytes:
        """
        Read uploaded file bytes.
        """

        content = await file.read()

        if not content:
            logger.error("Uploaded file is empty.")

            raise EmptyDocumentException()
            # raise HTTPException(
            #     status_code=400,
            #     detail="Uploaded file is empty.",
            # )

        return content

    def _validate(
        self,
        file: UploadFile,
    ) -> None:
        """
        Validate uploaded document.
        """

        if not file.filename:
            raise DocumentValidationException(
                "Filename is missing.")
            # raise HTTPException(
            #     status_code=400,
            #     detail="Filename is missing.",
            # )

        # extension = (
        #     "." +
        #     file.filename.split(".")[-1].lower()
        # )

        extension = Path(file.filename).suffix.lower()

        # if extension not in self.ALLOWED_EXTENSIONS:
        if extension not in SUPPORTED_DOCUMENT_TYPES:

            logger.error(
                "Unsupported file type: %s",
                extension,
            )

            raise UnsupportedDocumentException(
                f"Unsupported file type '{extension}'. "
                f"Supported formats: "
                f"{', '.join(sorted(SUPPORTED_DOCUMENT_TYPES))}"
                )