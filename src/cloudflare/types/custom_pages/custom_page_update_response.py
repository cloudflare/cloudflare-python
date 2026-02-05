# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["CustomPageUpdateResponse"]


class CustomPageUpdateResponse(BaseModel):
    id: Optional[str] = None

    created_on: Optional[datetime] = None

    description: Optional[str] = None

    modified_on: Optional[datetime] = None

    preview_target: Optional[str] = None

    required_tokens: Optional[List[str]] = None

    state: Optional[Literal["default", "customized"]] = None
    """The custom page state."""

    url: Optional[str] = None
    """The URL associated with the custom page."""
