from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path


@dataclass(slots=True)
class ParsedDocument:
    """
    Represents a parsed document extracted from an uploaded file.
    """

    filename: str
    extension: str
    text: str
    page_count: int
    character_count: int
    word_count: int

    extracted_at: datetime = field(default_factory=datetime.utcnow)

    @property
    def file_stem(self) -> str:
        """
        Returns filename without extension.
        """
        return Path(self.filename).stem
    
    @property
    def size_in_kb(self) -> float:
        """
        Returns the size of the document in kilobytes.
        """
        return round(self.character_count / 1024, 2)
    
    @property
    def is_empty(self) -> bool:
        """
        Returns whether the document is empty.
        """
        return len(self.text.strip()) == 0
    
    @property
    def summary(self) -> str:
        """
        Returns a summary of the document.
        """
        return self.text[:300]
    
    @property
    def file_type(self) -> str:
        return self.extension.replace(".", "").upper()