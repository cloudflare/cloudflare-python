# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["ObjectDeleteResponse"]


class ObjectDeleteResponse(BaseModel):
    """Result of a successful object deletion."""

    key: Optional[str] = None
    """The key (name) of the deleted object."""
