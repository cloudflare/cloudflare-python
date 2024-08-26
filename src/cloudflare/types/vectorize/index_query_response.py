# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional, List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["IndexQueryResponse", "Match"]

class Match(BaseModel):
    id: Optional[str] = None
    """Identifier for a Vector"""

    metadata: Optional[object] = None

    namespace: Optional[str] = None

    score: Optional[float] = None
    """The score of the vector according to the index's distance metric"""

    values: Optional[List[float]] = None

class IndexQueryResponse(BaseModel):
    count: Optional[int] = None
    """Specifies the count of vectors returned by the search"""

    matches: Optional[List[Match]] = None
    """Array of vectors matched by the search"""