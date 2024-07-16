# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SSLRecommender"]


class SSLRecommender(BaseModel):
    id: Optional[Literal["ssl_recommender"]] = None
    """Enrollment value for SSL/TLS Recommender."""

    enabled: Optional[bool] = None
    """ssl-recommender enrollment setting."""
