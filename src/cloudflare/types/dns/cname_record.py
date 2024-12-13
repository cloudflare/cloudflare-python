# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["CNAMERecord", "Settings"]


class Settings(BaseModel):
    flatten_cname: Optional[bool] = None
    """
    If enabled, causes the CNAME record to be resolved externally and the resulting
    address records (e.g., A and AAAA) to be returned instead of the CNAME record
    itself. This setting has no effect on proxied records, which are always
    flattened.
    """


class CNAMERecord(BaseModel):
    content: Optional[str] = None
    """A valid hostname. Must not match the record's name."""

    settings: Optional[Settings] = None

    type: Optional[Literal["CNAME"]] = None
    """Record type."""
