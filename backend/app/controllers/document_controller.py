# backend/app/controllers/document_controller.py
from fastapi import HTTPException, UploadFile, status

from app.config.logging_config import get_logger
from app.exceptions.document_exceptions import (
    DocumentException,
    DocumentValidationException,
    EmptyDocumentException,
    UnsupportedDocumentException,
)
from app.services.document_service import DocumentService

logger = get_logger(__name__)


class DocumentController:
    """
    Controller responsible for handling document-related requests.

    Responsibilities
    ----------------
    - Receive uploaded documents.
    - Delegate processing to DocumentService.
    - Convert domain objects into API responses.
    - Translate business exceptions into HTTP responses.
    """

    def __init__(
        self,
        document_service: DocumentService | None = None,
    ) -> None:

        self.document_service = (
            document_service or DocumentService()
        )

    async def upload_document(
        self,
        file: UploadFile,
    ) -> dict:
        """
        Upload and process a document.
        """

        logger.info(
            "Received upload request for '%s'.",
            file.filename,
        )

        try:

            document = await self.document_service.process_document(
                file
            )

            logger.info(
                "Document '%s' processed successfully.",
                document.filename,
            )

            return {
                "status": "success",
                "message": "Document processed successfully.",
                "document": {
                    "filename": document.filename,
                    "extension": document.extension,
                    "page_count": document.page_count,
                    "character_count": document.character_count,
                    "word_count": document.word_count,
                    "size_in_kb": document.size_in_kb,
                    "summary": document.summary,
                    "processed_at": document.extracted_at.isoformat(),
                },
            }

        except EmptyDocumentException as exc:

            logger.warning(str(exc))

            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(exc),
            )

        except UnsupportedDocumentException as exc:

            logger.warning(str(exc))

            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(exc),
            )

        except DocumentValidationException as exc:

            logger.warning(str(exc))

            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(exc),
            )

        except DocumentException as exc:

            logger.exception("Document processing failed.")

            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(exc),
            )

        except Exception:

            logger.exception(
                "Unexpected error while processing document."
            )

            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Internal server error.",
            )