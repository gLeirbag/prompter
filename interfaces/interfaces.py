from typing import Protocol

class DocumentsReader(Protocol):
    
    def __init__(self, path) -> None:
        ...

    def getDocument(self, filename) -> str:
        ...
        