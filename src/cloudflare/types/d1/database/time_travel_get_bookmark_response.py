# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["TimeTravelGetBookmarkResponse"]


class TimeTravelGetBookmarkResponse(BaseModel):
    bookmark: Optional[str] = None
    """
    A bookmark representing a specific state of the database at a specific point in
    time.
    """
