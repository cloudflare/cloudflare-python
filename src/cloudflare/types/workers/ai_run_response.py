# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional

from ..shared import UnnamedSchemaRef94, UnnamedSchemaRef135
from ..._models import BaseModel

__all__ = [
    "AIRunResponse",
    "TextEmbeddings",
    "SpeechRecognition",
    "ObjectDetection",
    "ObjectDetectionBox",
    "Response",
    "Translation",
    "Summarization",
    "ImageToText",
]


class TextEmbeddings(BaseModel):
    data: Optional[List[List[float]]] = None

    shape: Optional[List[float]] = None


class SpeechRecognition(BaseModel):
    text: str

    vtt: Optional[str] = None

    word_count: Optional[float] = None

    words: Optional[List[UnnamedSchemaRef94]] = None


class ObjectDetectionBox(BaseModel):
    xmax: Optional[float] = None

    xmin: Optional[float] = None

    ymax: Optional[float] = None

    ymin: Optional[float] = None


class ObjectDetection(BaseModel):
    box: Optional[ObjectDetectionBox] = None

    label: Optional[str] = None

    score: Optional[float] = None


class Response(BaseModel):
    response: Optional[str] = None


class Translation(BaseModel):
    translated_text: Optional[str] = None


class Summarization(BaseModel):
    summary: Optional[str] = None


class ImageToText(BaseModel):
    description: Optional[str] = None


AIRunResponse = Union[
    List[UnnamedSchemaRef135],
    object,
    List[float],
    TextEmbeddings,
    SpeechRecognition,
    List[UnnamedSchemaRef135],
    List[ObjectDetection],
    Response,
    object,
    Translation,
    Summarization,
    ImageToText,
]
