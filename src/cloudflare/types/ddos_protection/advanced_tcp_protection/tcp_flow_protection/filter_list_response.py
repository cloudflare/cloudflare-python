# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ....._models import BaseModel

__all__ = ["FilterListResponse"]


class FilterListResponse(BaseModel):
    id: str
    """The unique ID of the expression filter."""

    created_on: datetime
    """The creation timestamp of the expression filter."""

    expression: str
    """The filter expression."""

    mode: str
    """The filter's mode. Must be one of 'enabled', 'disabled', 'monitoring'."""

    modified_on: datetime
    """The last modification timestamp of the expression filter."""
