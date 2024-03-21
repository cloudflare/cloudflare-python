# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Required, TypedDict

from ..._types import FileTypes

__all__ = [
    "AIRunParams",
    "TextClassification",
    "TextToImage",
    "SentenceSimilarity",
    "TextEmbeddings",
    "Variant4",
    "Variant5",
    "Variant6",
    "Variant7",
    "Variant8",
    "Variant9",
    "Variant10",
    "Variant11",
    "Variant11Message",
    "Translation",
    "Summarization",
    "Variant14",
    "Variant15",
]


class TextClassification(TypedDict, total=False):
    account_id: Required[str]

    text: Required[str]


class TextToImage(TypedDict, total=False):
    account_id: Required[str]

    prompt: Required[str]

    guidance: float

    image: Iterable[float]

    mask: Iterable[float]

    num_steps: int

    strength: float


class SentenceSimilarity(TypedDict, total=False):
    account_id: Required[str]

    sentences: Required[List[str]]

    source: Required[str]


class TextEmbeddings(TypedDict, total=False):
    account_id: Required[str]

    text: Required[Union[str, List[str]]]


class Variant4(TypedDict, total=False):
    account_id: Required[str]

    body: Required[FileTypes]


class Variant5(TypedDict, total=False):
    account_id: Required[str]

    audio: Iterable[float]


class Variant6(TypedDict, total=False):
    account_id: Required[str]

    body: Required[FileTypes]


class Variant7(TypedDict, total=False):
    account_id: Required[str]

    image: Iterable[float]


class Variant8(TypedDict, total=False):
    account_id: Required[str]

    body: Required[FileTypes]


class Variant9(TypedDict, total=False):
    account_id: Required[str]

    image: Iterable[float]


class Variant10(TypedDict, total=False):
    account_id: Required[str]

    prompt: Required[str]

    lora: str

    max_tokens: int

    raw: bool

    stream: bool


class Variant11(TypedDict, total=False):
    account_id: Required[str]

    messages: Required[Iterable[Variant11Message]]

    max_tokens: int

    stream: bool


class Variant11Message(TypedDict, total=False):
    content: Required[str]

    role: Required[str]


class Translation(TypedDict, total=False):
    account_id: Required[str]

    target_lang: Required[str]

    text: Required[str]

    source_lang: str


class Summarization(TypedDict, total=False):
    account_id: Required[str]

    input_text: Required[str]

    max_length: int


class Variant14(TypedDict, total=False):
    account_id: Required[str]

    body: Required[FileTypes]


class Variant15(TypedDict, total=False):
    account_id: Required[str]

    image: Iterable[float]

    max_tokens: int

    prompt: str


AIRunParams = Union[
    TextClassification,
    TextToImage,
    SentenceSimilarity,
    TextEmbeddings,
    Variant4,
    Variant5,
    Variant6,
    Variant7,
    Variant8,
    Variant9,
    Variant10,
    Variant11,
    Translation,
    Summarization,
    Variant14,
    Variant15,
]
