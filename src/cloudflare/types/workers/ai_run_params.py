# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, TypeAlias

from typing import Iterable, Union, List, Dict

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo

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
    "Variant7Function",
    "Variant7Tool",
    "Variant7ToolUnionMember0",
    "Variant7ToolUnionMember0Parameters",
    "Variant7ToolUnionMember0ParametersProperties",
    "Variant7ToolUnionMember1",
    "Variant7ToolUnionMember1Function",
    "Variant7ToolUnionMember1FunctionParameters",
    "Variant7ToolUnionMember1FunctionParametersProperties",
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

    functions: Iterable[Variant7Function]

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


class Variant7Function(TypedDict, total=False):
    code: Required[str]

    name: Required[str]


class Variant7ToolUnionMember0ParametersProperties(TypedDict, total=False):
    description: Required[str]

    type: Required[str]


class Variant7ToolUnionMember0Parameters(TypedDict, total=False):
    properties: Required[Dict[str, Variant7ToolUnionMember0ParametersProperties]]

    type: Required[str]

    required: List[str]


class Variant7ToolUnionMember0(TypedDict, total=False):
    description: Required[str]

    name: Required[str]

    parameters: Required[Variant7ToolUnionMember0Parameters]


class Variant7ToolUnionMember1FunctionParametersProperties(TypedDict, total=False):
    description: Required[str]

    type: Required[str]


class Variant7ToolUnionMember1FunctionParameters(TypedDict, total=False):
    properties: Required[Dict[str, Variant7ToolUnionMember1FunctionParametersProperties]]

    type: Required[str]

    required: List[str]


class Variant7ToolUnionMember1Function(TypedDict, total=False):
    description: Required[str]

    name: Required[str]

    parameters: Required[Variant7ToolUnionMember1FunctionParameters]


class Variant7ToolUnionMember1(TypedDict, total=False):
    function: Required[Variant7ToolUnionMember1Function]

    type: Required[str]


Variant7Tool: TypeAlias = Union[Variant7ToolUnionMember0, Variant7ToolUnionMember1]


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


AIRunParams: TypeAlias = Union[
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
