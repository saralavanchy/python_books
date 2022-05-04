from pydantic import BaseModel
from enum import Enum
from typing import List, Optional, Union

class BibleBookType(enum):
    LAW
    WISDOM_LITERATURE
    PSALMS
    NOVELLA
    PROPHECY
    APOCALYPTIC_LETERATURE
    GOSPEL
    ACTS_OF_THE_APOSTLES
    EPISTLE

class Chaper(BaseModel):
    number: int
    numberOfVerses: int

    def hasVerse(self, verse: int) -> bool:
        return verse <= self.numberOfVerses

    def __eq__(self, chapter: Union[int, Chaper]):
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