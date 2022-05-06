from pydantic import BaseModel
from enum import Enum
from typing import List, Optional, Union

class BibleBookType(Enum):
    LAW = "Law"
    WISDOM = "Wisdom literature"
    PSALMS = "Psalms"
    NOVELLA = "Novella"
    PROPHECY = "Prophecy"
    APOCALYPTIC = "Apocalyptic literature"
    GOSPEL = "Gospel"
    ACTS = "Acts of the apostoles"
    EPISTLE = "Epistles"

class Chaper(BaseModel):
    number: int
    numberOfVerses: int

    def hasVerse(self, verse: int) -> bool:
        return verse <= self.numberOfVerses

    def __eq__(self, chapter: Union[int, Chapter]):
        if isinstance(chapter, Chaper):
            return chapter.number == self.number
        return chapter == self.number

class Book(BaseModel):
    name: str
    chapters: List[Chaper]
    description: Optional[str] = ""
    type: Optional[BibleBookType] = None

    def hasChapter(self, chapter:int) -> bool:
        return chapter in self.chapters

class Testament(BaseModel):
    name: str
    books: List[Book]

class BibleText(BaseModel):
    book: str
    chapter: int
    verseFrom: int
    verseTo: int
    text: str