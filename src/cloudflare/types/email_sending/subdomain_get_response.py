# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["SubdomainGetResponse"]


class SubdomainGetResponse(BaseModel):
    enabled: bool
    """Whether Email Sending is enabled on this subdomain."""

    name: str
    """The subdomain domain name."""

    tag: str
    """Sending subdomain identifier."""

    created: Optional[datetime] = None
    """The date and time the destination address has been created."""

    dkim_selector: Optional[str] = None
    """The DKIM selector used for email signing."""

    modified: Optional[datetime] = None
    """The date and time the destination address was last modified."""

    return_path_domain: Optional[str] = None
    """The return-path domain used for bounce handling."""
