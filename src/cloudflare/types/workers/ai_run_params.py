# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from typing_extensions import Required, TypedDict

__all__ = [
    "AIRunParams",
    "TextClassification",
    "TextToImage",
    "TextEmbeddings",
    "AutomaticSpeechRecognition",
    "ImageClassification",
    "ObjectDetection",
    "Variant6",
    "Variant7",
    "Variant7Message",
    "Variant7Tool",
    "Variant7ToolFunction",
    "Variant7ToolFunctionParameters",
    "Variant7ToolFunctionParametersProperties",
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

    height: int

    image: Iterable[float]

    image_b64: str

    mask: Iterable[float]

    negative_prompt: str

    num_steps: int

    seed: int

    strength: float

    width: int


class TextEmbeddings(TypedDict, total=False):
    account_id: Required[str]

    text: Required[Union[str, List[str]]]


class AutomaticSpeechRecognition(TypedDict, total=False):
    account_id: Required[str]

    audio: Required[Iterable[float]]


class ImageClassification(TypedDict, total=False):
    account_id: Required[str]

    image: Required[Iterable[float]]


class ObjectDetection(TypedDict, total=False):
    account_id: Required[str]

    image: Iterable[float]


class Variant6(TypedDict, total=False):
    account_id: Required[str]

    prompt: Required[str]

    frequency_penalty: float

    lora: str

    max_tokens: int

    presence_penalty: float

    raw: bool

    repetition_penalty: float

    seed: int

    stream: bool

    temperature: float

    top_k: int

    top_p: float


class Variant7(TypedDict, total=False):
    account_id: Required[str]

    messages: Required[Iterable[Variant7Message]]

    frequency_penalty: float

    max_tokens: int

    presence_penalty: float

    repetition_penalty: float

    seed: int

    stream: bool

    temperature: float

    tools: Iterable[Variant7Tool]

    top_k: int

    top_p: float


class Variant7Message(TypedDict, total=False):
    content: Required[str]

    role: Required[str]


class Variant7ToolFunctionParametersProperties(TypedDict, total=False):
    description: str

    type: str


class Variant7ToolFunctionParameters(TypedDict, total=False):
    properties: Dict[str, Variant7ToolFunctionParametersProperties]

    required: List[str]

    type: str


class Variant7ToolFunction(TypedDict, total=False):
    description: str

    name: str

    parameters: Variant7ToolFunctionParameters


class Variant7Tool(TypedDict, total=False):
    function: Variant7ToolFunction

    type: str


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
    TextEmbeddings,
    AutomaticSpeechRecognition,
    ImageClassification,
    ObjectDetection,
    Variant6,
    Variant7,
    Translation,
    Summarization,
    ImageToText,
]
