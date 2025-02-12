"""
The MIT License (MIT)

Copyright (c) 2021-Present AbstractUmbra

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

from typing import Literal, Optional, TypedDict

from .relationship import RelationshipResponse


__all__ = ("GetChapterFeedResponse", "ChapterAttributesResponse")


class ChapterAttributesOptionalResponse(TypedDict, total=False):
    uploader: Optional[str]


class ChapterAttributesResponse(ChapterAttributesOptionalResponse):
    title: Optional[str]
    volume: Optional[str]
    chapter: Optional[str]
    translatedLanguage: str
    hash: str
    data: list[str]
    dataSaver: list[str]
    version: int
    createdAt: str
    updatedAt: str
    publishAt: str


class ChapterResponse(TypedDict):
    id: str
    type: Literal["chapter"]
    attributes: ChapterAttributesResponse


class GetChapterResponse(TypedDict):
    result: Literal["ok", "err"]
    data: ChapterResponse
    relationships: list[RelationshipResponse]


class GetChapterFeedResponse(TypedDict):
    results: list[GetChapterResponse]
    limit: int
    offset: int
    total: int
