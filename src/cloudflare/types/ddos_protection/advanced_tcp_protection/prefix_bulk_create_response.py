# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ...._models import BaseModel

__all__ = ["PrefixBulkCreateResponse"]


class PrefixBulkCreateResponse(BaseModel):
    id: str
    """The unique ID of the prefix."""

    comment: str
    """A comment describing the prefix."""

    created_on: datetime
    """The creation timestamp of the prefix."""

    excluded: bool
    """Whether to exclude the prefix from protection."""

    modified_on: datetime
    """The last modification timestamp of the prefix."""

    prefix: str
    """The prefix in CIDR format."""
