# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = [
    "ScrapeCreateResponse",
    "ScrapeCreateResponseItem",
    "ScrapeCreateResponseItemResults",
    "ScrapeCreateResponseItemResultsAttribute",
]


class ScrapeCreateResponseItemResultsAttribute(BaseModel):
    name: str
    """Attribute name"""

    value: str
    """Attribute value"""


class ScrapeCreateResponseItemResults(BaseModel):
    attributes: List[ScrapeCreateResponseItemResultsAttribute]

    height: float
    """Element height"""

    html: str
    """Html content"""

    left: float
    """Element left"""

    text: str
    """Text content"""

    top: float
    """Element top"""

    width: float
    """Element width"""


class ScrapeCreateResponseItem(BaseModel):
    results: ScrapeCreateResponseItemResults

    selector: str
    """Selector"""


ScrapeCreateResponse: TypeAlias = List[ScrapeCreateResponseItem]
