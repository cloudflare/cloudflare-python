# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional

from ..._models import BaseModel

__all__ = [
    "AIRunResponse",
    "TextClassification",
    "TextEmbeddings",
    "SpeechRecognition",
    "SpeechRecognitionWord",
    "ImageClassification",
    "ObjectDetection",
    "ObjectDetectionBox",
    "Response",
    "Translation",
    "Summarization",
    "ImageToText",
]


class TextClassification(BaseModel):
    label: Optional[str] = None

    score: Optional[float] = None


class TextEmbeddings(BaseModel):
    data: Optional[List[List[float]]] = None

    shape: Optional[List[float]] = None


class SpeechRecognitionWord(BaseModel):
    end: Optional[float] = None

    start: Optional[float] = None

    word: Optional[str] = None


class SpeechRecognition(BaseModel):
    text: str

    vtt: Optional[str] = None

    word_count: Optional[float] = None

    words: Optional[List[SpeechRecognitionWord]] = None


class ImageClassification(BaseModel):
    label: Optional[str] = None

    score: Optional[float] = None


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
    List[TextClassification],
    object,
    List[float],
    TextEmbeddings,
    SpeechRecognition,
    List[ImageClassification],
    List[ObjectDetection],
    Response,
    object,
    Translation,
    Summarization,
    ImageToText,
]
