# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["FallbackDomain"]


class FallbackDomain(BaseModel):
    suffix: str
    """The domain suffix to match when resolving locally."""

    description: Optional[str] = None
    """A description of the fallback domain, displayed in the client UI."""

    dns_server: Optional[List[str]] = None
    """A list of IP addresses to handle domain resolution."""
