# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = [
    "AIRunResponse",
    "TextClassification",
    "TextEmbeddings",
    "AutomaticSpeechRecognition",
    "AutomaticSpeechRecognitionWord",
    "ImageClassification",
    "ObjectDetection",
    "ObjectDetectionBox",
    "UnionMember6",
    "UnionMember6ToolCall",
    "Translation",
    "Summarization",
    "ImageToText",
]


class TextClassification(BaseModel):
    label: Optional[str] = None
    """The classification label assigned to the text (e.g., 'POSITIVE' or 'NEGATIVE')"""

    score: Optional[float] = None
    """
    Confidence score indicating the likelihood that the text belongs to the
    specified label
    """


class TextEmbeddings(BaseModel):
    data: Optional[List[List[float]]] = None
    """Embeddings of the requested text values"""

    shape: Optional[List[float]] = None


class AutomaticSpeechRecognitionWord(BaseModel):
    end: Optional[float] = None
    """The ending second when the word completes"""

    start: Optional[float] = None
    """The second this word begins in the recording"""

    word: Optional[str] = None


class AutomaticSpeechRecognition(BaseModel):
    text: str
    """The transcription"""

    vtt: Optional[str] = None

    word_count: Optional[float] = None

    words: Optional[List[AutomaticSpeechRecognitionWord]] = None


class ImageClassification(BaseModel):
    label: Optional[str] = None
    """The predicted category or class for the input image based on analysis"""

    score: Optional[float] = None
    """
    A confidence value, between 0 and 1, indicating how certain the model is about
    the predicted label
    """


class ObjectDetectionBox(BaseModel):
    xmax: Optional[float] = None
    """The x-coordinate of the bottom-right corner of the bounding box"""

    xmin: Optional[float] = None
    """The x-coordinate of the top-left corner of the bounding box"""

    ymax: Optional[float] = None
    """The y-coordinate of the bottom-right corner of the bounding box"""

    ymin: Optional[float] = None
    """The y-coordinate of the top-left corner of the bounding box"""


class ObjectDetection(BaseModel):
    box: Optional[ObjectDetectionBox] = None
    """Coordinates defining the bounding box around the detected object"""

    label: Optional[str] = None
    """The class label or name of the detected object"""

    score: Optional[float] = None
    """Confidence score indicating the likelihood that the detection is correct"""


class UnionMember6ToolCall(BaseModel):
    arguments: Optional[object] = None
    """The arguments passed to be passed to the tool call request"""

    name: Optional[str] = None
    """The name of the tool to be called"""


class UnionMember6(BaseModel):
    response: Optional[str] = None
    """The generated text response from the model"""

    tool_calls: Optional[List[UnionMember6ToolCall]] = None
    """An array of tool calls requests made during the response generation"""


class Translation(BaseModel):
    translated_text: Optional[str] = None
    """The translated text in the target language"""


class Summarization(BaseModel):
    summary: Optional[str] = None
    """The summarized version of the input text"""


class ImageToText(BaseModel):
    description: Optional[str] = None


AIRunResponse: TypeAlias = Union[
    List[TextClassification],
    object,
    TextEmbeddings,
    AutomaticSpeechRecognition,
    List[ImageClassification],
    List[ObjectDetection],
    UnionMember6,
    Translation,
    Summarization,
    ImageToText,
]
