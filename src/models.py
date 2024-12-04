from __future__ import annotations
from pydantic import BaseModel
from typing import List

class CrowdAnkiNote(BaseModel):
    fields: List[str]


class CrowdAnkiJson(BaseModel):
    name: str
    children: List[CrowdAnkiJson]
    notes: List[CrowdAnkiNote]


class OutputNote(BaseModel):
    source: str
    target: str
    deck_name: str

    def toOutputString(self) -> str:
        return f'{{"source":"{self.source}","target":"{self.target}","deck_name":"{self.deck_name}"}}'