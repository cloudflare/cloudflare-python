# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = [
    "BrowserRenderingScrapeResponse",
    "BrowserRenderingScrapeResponseItem",
    "BrowserRenderingScrapeResponseItemResult",
    "BrowserRenderingScrapeResponseItemResultAttribute",
]


class BrowserRenderingScrapeResponseItemResultAttribute(BaseModel):
    name: str
    """Attribute name"""

    value: str
    """Attribute value"""


class BrowserRenderingScrapeResponseItemResult(BaseModel):
    attributes: List[BrowserRenderingScrapeResponseItemResultAttribute]

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


class BrowserRenderingScrapeResponseItem(BaseModel):
    result: BrowserRenderingScrapeResponseItemResult

    selector: str
    """Selector"""


BrowserRenderingScrapeResponse: TypeAlias = List[BrowserRenderingScrapeResponseItem]
