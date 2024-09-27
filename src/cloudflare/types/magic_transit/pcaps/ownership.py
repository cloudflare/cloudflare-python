# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["Ownership"]


class Ownership(BaseModel):
    id: str
    """The bucket ID associated with the packet captures API."""

    destination_conf: str
    """The full URI for the bucket. This field only applies to `full` packet captures."""

    filename: str
    """The ownership challenge filename stored in the bucket."""

    status: Literal["pending", "success", "failed"]
    """The status of the ownership challenge. Can be pending, success or failed."""

    submitted: str
    """The RFC 3339 timestamp when the bucket was added to packet captures API."""

    validated: Optional[str] = None
    """The RFC 3339 timestamp when the bucket was validated."""
