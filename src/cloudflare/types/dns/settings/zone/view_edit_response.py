# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from ....._models import BaseModel

__all__ = ["ViewEditResponse"]


class ViewEditResponse(BaseModel):
    id: str
    """Identifier"""

    created_time: datetime
    """When the view was created."""

    modified_time: datetime
    """When the view was last modified."""

    name: str
    """The name of the view."""

    zones: List[str]
    """The list of zones linked to this view."""
