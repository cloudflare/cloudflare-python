# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Required, TypedDict

__all__ = [
    "AIRunParams",
    "TextClassification",
    "TextToImage",
    "SentenceSimilarity",
    "TextEmbeddings",
    "SpeechRecognition",
    "ImageClassification",
    "ObjectDetection",
    "TextGeneration",
    "TextGenerationMessage",
    "Translation",
    "Summarization",
    "ImageToText",
    "ImageToTextMessage",
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


class SpeechRecognition(TypedDict, total=False):
    account_id: Required[str]

    audio: Required[Iterable[float]]


class ImageClassification(TypedDict, total=False):
    account_id: Required[str]

    image: Required[Iterable[float]]


class ObjectDetection(TypedDict, total=False):
    account_id: Required[str]

    image: Iterable[float]


class TextGeneration(TypedDict, total=False):
    account_id: Required[str]

    lora: str

    max_tokens: int

    messages: Iterable[TextGenerationMessage]

    prompt: str

    raw: bool

    stream: bool


class TextGenerationMessage(TypedDict, total=False):
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


class ImageToText(TypedDict, total=False):
    account_id: Required[str]

    image: Required[Iterable[float]]

    max_tokens: int

    messages: Iterable[ImageToTextMessage]

    prompt: str

    raw: bool

    temperature: float


class ImageToTextMessage(TypedDict, total=False):
    content: Required[str]

    role: Required[str]


AIRunParams = Union[
    TextClassification,
    TextToImage,
    SentenceSimilarity,
    TextEmbeddings,
    SpeechRecognition,
    ImageClassification,
    ObjectDetection,
    TextGeneration,
    Translation,
    Summarization,
    ImageToText,
]
