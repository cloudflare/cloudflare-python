# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Required, TypedDict

from ..._types import FileTypes

__all__ = [
    "AIRunParams",
    "Body",
    "BodyTextClassification",
    "BodyTextToImage",
    "BodySentenceSimilarity",
    "BodyTextEmbeddings",
    "BodyAudio",
    "BodyImage",
    "BodyUnionMember10",
    "BodyUnionMember11",
    "BodyUnionMember11Message",
    "BodyTranslation",
    "BodySummarization",
    "BodyUnionMember15",
]


class AIRunParams(TypedDict, total=False):
    account_id: Required[str]

    body: Required[Body]


class BodyTextClassification(TypedDict, total=False):
    text: Required[str]


class BodyTextToImage(TypedDict, total=False):
    prompt: Required[str]

    guidance: float

    image: Iterable[float]

    mask: Iterable[float]

    num_steps: int

    strength: float


class BodySentenceSimilarity(TypedDict, total=False):
    sentences: Required[List[str]]

    source: Required[str]


class BodyTextEmbeddings(TypedDict, total=False):
    text: Required[Union[str, List[str]]]


class BodyAudio(TypedDict, total=False):
    audio: Iterable[float]


class BodyImage(TypedDict, total=False):
    image: Iterable[float]


class BodyImage(TypedDict, total=False):
    image: Iterable[float]


class BodyUnionMember10(TypedDict, total=False):
    prompt: Required[str]

    max_tokens: int

    raw: bool

    stream: bool


class BodyUnionMember11Message(TypedDict, total=False):
    content: Required[str]

    role: Required[str]


class BodyUnionMember11(TypedDict, total=False):
    messages: Required[Iterable[BodyUnionMember11Message]]

    max_tokens: int

    stream: bool


class BodyTranslation(TypedDict, total=False):
    target_lang: Required[str]

    text: Required[str]

    source_lang: str


class BodySummarization(TypedDict, total=False):
    input_text: Required[str]

    max_length: int


class BodyUnionMember15(TypedDict, total=False):
    image: Iterable[float]

    max_tokens: int

    prompt: str


Body = Union[
    BodyTextClassification,
    BodyTextToImage,
    BodySentenceSimilarity,
    BodyTextEmbeddings,
    FileTypes,
    BodyAudio,
    FileTypes,
    BodyImage,
    FileTypes,
    BodyImage,
    BodyUnionMember10,
    BodyUnionMember11,
    BodyTranslation,
    BodySummarization,
    FileTypes,
    BodyUnionMember15,
]
