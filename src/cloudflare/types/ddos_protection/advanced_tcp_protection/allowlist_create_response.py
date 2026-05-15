# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ...._models import BaseModel

__all__ = ["AllowlistCreateResponse"]


class AllowlistCreateResponse(BaseModel):
    id: str
    """The unique ID of the allowlist prefix."""

    comment: str
    """An optional comment describing the allowlist prefix."""

    created_on: datetime
    """The creation timestamp of the allowlist prefix."""

    enabled: bool
    """Whether to enable the allowlist prefix into effect. Defaults to false."""

    modified_on: datetime
    """The last modification timestamp of the allowlist prefix."""

    prefix: str
    """The allowlist prefix in CIDR format."""
