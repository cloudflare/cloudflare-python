# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from typing_extensions import Literal

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..._models import BaseModel
from ...types import shared

__all__ = ["SSLRecommenderGetResponse"]


class SSLRecommenderGetResponse(BaseModel):
    id: Optional[Literal["ssl_recommender"]] = None
    """Enrollment value for SSL/TLS Recommender."""

    enabled: Optional[bool] = None
    """ssl-recommender enrollment setting."""
